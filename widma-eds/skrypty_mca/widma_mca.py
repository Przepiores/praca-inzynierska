# Widma EDS z plików .mca (KETEK DPP2 / ProSpect v1.1.36): kalibracja, piki, wykresy.
# Uruchomienie: python3 -I widma_mca.py <katalog widma-eds>
# Wyjście: widma_materialy.pdf/png, widmo_eds_4kV.pdf/png, widma_csv/*.csv, piki_13-11.csv
import sys, os, glob, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt, matplotlib.ticker as tk
from scipy.optimize import curve_fit

BASE = sys.argv[1] if len(sys.argv) > 1 else '/mnt/project-files/widma-eds'
D = os.path.join(BASE, 'dane_mca')
N, EMAX = 8192, 80.0
E_RAW = np.arange(N) * EMAX / N            # skala z pliku: kanał * 80/8192 keV

def read(p):
    L = open(p, encoding='utf-8', errors='replace').read().replace('\r', '').split('\n')
    h = {}
    for i, l in enumerate(L):
        if l.strip() == str(N) and i > 0 and L[i-1].strip() == '':
            y = np.array([float(x) for x in L[i+1:i+1+N]]); return h, y
        if '=' in l:
            k, v = l.split('=', 1); h[k.strip().rstrip(':').strip()] = v.strip()
    raise ValueError(p)

def num(h, k): return float(h[k].split()[0])

def gfit(E, y, e0, w):
    f = lambda x, A, m, s, a, b: A*np.exp(-(x-m)**2/(2*s*s)) + a + b*(x-m)
    m = (E > e0-w) & (E < e0+w); x, yy = E[m], y[m]
    p, _ = curve_fit(f, x, yy, p0=[yy.max()-yy.min(), x[np.argmax(yy)], 0.04, yy.min(), 0], maxfev=20000)
    return p[1], abs(p[2])*2.3548, p[0]

def total(files):
    y = 0; lt = 0
    for f in files: h, s = read(f); y = y + s; lt += num(h, 'Live Time')
    return y, lt

S13 = os.path.join(D, '2026-11-13')
G = {
    'miedz':  sorted(glob.glob(f'{S13}/miedz/*.mca')),
    'olow':   sorted(glob.glob(f'{S13}/olow/*.mca')),
    'final':  sorted(glob.glob(f'{S13}/final/*.mca')),
    # Al: tylko seria9 (najmniejszy czas martwy, 20 %); seria2-3 mają czas martwy >90 %, seria11 = kopia seria10
    'aluminium': [f'{S13}/aluminium/seria9.mca'],
}
Y = {k: total(v) for k, v in G.items()}

# --- kalibracja liniowa 13.11: E = a*E_raw + b, linie o pewnej identyfikacji ---
ref = [('aluminium', 1.47, 1.4866, 'Al Ka'), ('olow', 2.31, 2.3455, 'Pb Ma'),
       ('final', 5.32, 5.4147, 'Cr Ka'), ('aluminium', 6.29, 6.3999, 'Fe Ka'), ('miedz', 7.89, 8.0411, 'Cu Ka')]
mr = np.array([gfit(E_RAW, Y[g][0], e, 0.12)[0] for g, e, _, _ in ref]); tr = np.array([t for _, _, t, _ in ref])
a, b = np.polyfit(mr, tr, 1); res = (a*mr + b - tr)*1000
print(f'kalibracja 13.11: E = {a:.5f}*E_raw {b:+.5f} keV; residua [eV]:', np.round(res, 1))
E = a*E_RAW + b

# --- piki (położenie po kalibracji, FWHM) ---
PK = {'miedz': [(0.92,'Cu La',0.930),(1.47,'Al Ka',1.487),(1.72,'Si Ka',1.740),(1.98,'P Ka',2.013),(2.27,'S Ka',2.307),
               (2.58,'Cl Ka',2.622),(3.26,'K Ka',3.313),(3.70,'Te La',3.769),(3.96,'Te Lb1',4.029),(4.23,'Te Lb2',4.302),
               (4.49,'Te Lg1',4.571),(7.89,'Cu Ka',8.041),(8.73,'Cu Kb',8.905)],
      'olow': [(1.81,'Pb Mz',1.841),(2.31,'Pb Ma',2.346),(2.61,'Pb Mg',2.653)],
      'final': [(0.94,'Cu La',0.930),(1.64,'Au Mz',1.660),(2.11,'Au Ma+Mb',2.140),(2.38,'Au Mg',2.409),(2.75,'Au M2N4',2.795),
                (5.32,'Cr Ka',5.415),(5.85,'Cr Kb',5.947),(7.89,'Cu Ka',8.041)],
      'aluminium': [(1.47,'Al Ka',1.487),(2.93,'2xAl Ka (sum.)',2.973),(5.80,'Mn Ka',5.899),(6.29,'Fe Ka',6.400)]}
os.makedirs(f'{BASE}/widma_csv', exist_ok=True)
with open(f'{BASE}/piki_13-11.csv', 'w') as fo:
    fo.write('probka;linia;E_zmierz_keV;E_tabel_keV;roznica_eV;FWHM_eV;amplituda\n')
    for g, lst in PK.items():
        for e, lab, et in lst:
            m, fw, A = gfit(E_RAW, Y[g][0], e, 0.08 if lab=='Te Lb2' else (0.10 if e < 3 else 0.15))
            fo.write(f'{g};{lab};{a*m+b:.3f};{et:.3f};{(a*m+b-et)*1000:.0f};{fw*a*1000:.0f};{A:.0f}\n')
for g, (y, lt) in Y.items():
    np.savetxt(f'{BASE}/widma_csv/{g}_13-11.csv', np.c_[E, y], delimiter=';', fmt=['%.4f', '%d'],
               header=f'E_keV;zliczenia (suma: {", ".join(os.path.basename(f) for f in G[g])}; live {lt:.1f} s)', comments='')

# ------------------------------- wykresy -------------------------------
# czcionka bezszeryfowa (uwagi z prezentacji 23.11): TeX Gyre Heros, jak \sffamily na rysunkach TikZ
plt.rcParams.update({'font.family': ['TeX Gyre Heros', 'DejaVu Sans'], 'font.size': 9, 'axes.formatter.use_locale': False,
                     'mathtext.fontset': 'custom', 'mathtext.rm': 'TeX Gyre Heros', 'mathtext.it': 'TeX Gyre Heros:italic',
                     'mathtext.bf': 'TeX Gyre Heros:bold', 'mathtext.sf': 'TeX Gyre Heros', 'pdf.fonttype': 42})
C = '#1f5fa8'; R = '#c0392b'; GR = '#7f7f7f'
comma = tk.FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ','))
def pw10(ax):
    ax.yaxis.set_major_formatter(tk.FuncFormatter(lambda v, p: f'$10^{{{int(round(np.log10(v)))}}}$' if v > 0 else ''))

LAB = {  # (E tabel., etykieta, przesunięcie pionowe w pkt)
 'miedz': [(0.930,'Cu L$\\alpha$',4),(1.740,'Si',4),(2.013,'P',4),(2.307,'S',4),(2.622,'Cl',4),(3.313,'K',4),
           (3.769,'Te L$\\alpha$',4),(4.029,'L$\\beta_1$',13),(4.302,'L$\\beta_2$',4),(1.487,'Al',4),(8.041,'Cu K$\\alpha$',4),(8.905,'Cu K$\\beta$',4)],
 'olow': [(1.841,'Pb M$\\zeta$',4),(2.346,'Pb M$\\alpha$',4),(2.653,'Pb M$\\gamma$',14)],
 'final': [(0.930,'Cu L$\\alpha$',4),(1.660,'Au M$\\zeta$',4),(2.123,'Au M$\\alpha$',4),(2.409,'Au M$\\gamma$',14),
           (5.415,'Cr K$\\alpha$',4),(5.947,'Cr K$\\beta$',4),(8.041,'Cu K$\\alpha$',4)],
 'aluminium': [(1.487,'Al K$\\alpha$',4),(2.973,'2·Al (sum.)',4),(4.46,'3·Al',4),(5.899,'Mn',14),(6.400,'Fe K$\\alpha$',4)]}
TIT = {'miedz': '(a) próbka A: Cu z zanieczyszczeniami', 'olow': '(b) próbka B: Pb',
       'final': '(c) próbka C: Au, Cr, Cu', 'aluminium': '(d) próbka D: Al'}

PANELE = ['miedz', 'olow', 'final']   # próbkę Al opisano w tekście (widmo podobne do rys. 4 kV)
fig, axs = plt.subplots(len(PANELE), 1, figsize=(6.3, 6.0), sharex=True)
for ax, g in zip(axs, PANELE):
    y, lt = Y[g]; r = y/lt
    ax.semilogy(E, np.where(r > 0, r, np.nan), color=C, lw=0.7)
    top = np.nanmax(r[(E > 0.3) & (E < 10)])
    ax.set_ylim(top*1e-4, top*6); ax.set_xlim(0.3, 10)
    ax.axvspan(0.3, 0.65, color=GR, alpha=0.15, lw=0)
    ax.axvline(0.525, color=R, ls='--', lw=0.8)
    for e, t, dy in LAB[g]:
        i = np.argmin(abs(E-e)); yy = r[max(i-4,0):i+5].max()
        ax.annotate(t, (e, yy), xytext=(0, dy), textcoords='offset points', ha='center', fontsize=7)
    ax.text(0.99, 0.92, TIT[g], transform=ax.transAxes, ha='right', va='top', fontsize=8)
    ax.grid(alpha=0.25, which='major'); pw10(ax); ax.yaxis.set_minor_formatter(tk.NullFormatter())
    ax.set_ylabel('zliczenia / (s·kanał)', fontsize=8)
axs[1].text(0.40, 0.5, 'poza zakresem rejestracji', transform=axs[1].get_xaxis_transform(), fontsize=6.5, color='#555555', ha='center', va='center', rotation=90)
axs[0].text(0.545, 0.45, 'O K$\\alpha$ 0,525 keV', color=R, fontsize=7, ha='left', rotation=90, transform=axs[0].get_xaxis_transform())
axs[-1].set_xlabel('Energia fotonu $E$ [keV]'); axs[-1].xaxis.set_major_formatter(comma)
axs[-1].set_xticks([0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fig.tight_layout(h_pad=0.4)
fig.savefig(f'{BASE}/widma_materialy.pdf'); fig.savefig(f'{BASE}/widma_materialy.png', dpi=200)

# --- widmo 12.06 (Al, 4 kV) z natywnego pliku 4SERIA.mca (to samo co na zdjęciu: real 210,7 s, live 100,1 s) ---
h, y = read(f'{D}/2026-06-12_Al_4kV/4SERIA.mca')
mr2 = np.array([gfit(E_RAW, y, e, 0.08)[0] for e in (1.23, 1.46, 1.70)])
a2, b2 = np.polyfit(mr2, [1.2536, 1.4866, 1.7398], 1); E2 = a2*E_RAW + b2
print(f'kalibracja 12.06: E = {a2:.5f}*E_raw {b2:+.5f}; residua [eV]:', np.round((a2*mr2+b2-[1.2536,1.4866,1.7398])*1000, 1))
np.savetxt(f'{BASE}/widma_csv/al_4kV_12-06_4SERIA.csv', np.c_[E2, y], delimiter=';', fmt=['%.4f', '%d'],
           header='E_keV;zliczenia (4SERIA.mca, live 100,05 s)', comments='')
fig, ax = plt.subplots(figsize=(6.3, 3.4))
ax.plot(E2, y/1e3, color=C, lw=1.0)
for e, t in [(1.254, 'Mg K$\\alpha$\n1,254'), (1.487, 'Al K$\\alpha$\n1,486'), (1.740, 'Si K$\\alpha$\n1,740')]:
    i = np.argmin(abs(E2-e)); ax.annotate(t, (e, y[i-3:i+4].max()/1e3), xytext=(0, 4), textcoords='offset points', ha='center', fontsize=7.5)
ax.axvline(4.0, color=GR, ls='--', lw=0.8); ax.text(4.05, 1250, '$eU_\\mathrm{T}$ = 4 keV\n(granica Duane’a–Hunta)', fontsize=7.5, color=GR)
ax.set_xlim(0, 6); ax.set_ylim(0, 1550); ax.grid(alpha=0.25)
ax.set_xlabel('Energia fotonu $E$ [keV]'); ax.set_ylabel('Liczba zliczeń [10$^3$ / kanał]'); ax.xaxis.set_major_formatter(comma)
ins = ax.inset_axes([0.55, 0.36, 0.42, 0.32]); m = (E2 > 2.2) & (E2 < 4.6)
ins.plot(E2[m], y[m]/1e3, color=C, lw=0.9)
for e, t, ha in [(2.973, '2·Al', 'right'), (3.226, 'Al+Si', 'center'), (3.480, '2·Si', 'left')]:
    ins.axvline(e, color=R, lw=0.6, ls=':'); ins.text(e, 27, t, fontsize=6.5, ha=ha, color=R)
ins.set_ylim(0, 30); ins.tick_params(labelsize=7); ins.xaxis.set_major_formatter(comma)
ins.set_title('powiększenie 2,2–4,6 keV: piki sumacyjne', fontsize=7)
fig.tight_layout(); fig.savefig(f'{BASE}/widmo_eds_4kV.pdf'); fig.savefig(f'{BASE}/widmo_eds_4kV.png', dpi=200)
for e in (1.23, 1.46, 1.70):
    m, fw, A = gfit(E_RAW, y, e, 0.08); i = np.argmin(abs(E_RAW-m)); print(f'12.06 pik {a2*m+b2:.3f} keV, FWHM {fw*a2*1000:.0f} eV, max {int(y[i-2:i+3].max())}')
