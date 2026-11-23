# Stabilność zliczeń podczas pomiaru 12.06.2026 (odczyty ze zdjęć ekranu ProSpect).
# Uruchomienie: python3 -I stabilnosc.py <katalog widma-eds>   -> stabilnosc_zliczen.pdf/png
import sys, os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
BASE = sys.argv[1] if len(sys.argv) > 1 else '/mnt/project-files/widma-eds'
plt.rcParams.update({'font.family': ['TeX Gyre Heros', 'DejaVu Sans'], 'font.size': 10, 'axes.formatter.use_locale': False,
                     'mathtext.fontset': 'custom', 'mathtext.rm': 'TeX Gyre Heros', 'mathtext.it': 'TeX Gyre Heros:italic',
                     'mathtext.bf': 'TeX Gyre Heros:bold', 'mathtext.sf': 'TeX Gyre Heros', 'pdf.fonttype': 42})
# stability
rows=[(22.171,10.266,5040564,490.9824,227.3498,54,153885),(43.479,20.332,9861175,484.9997,226.8010,53,297351),(83.342,39.801,18751443,471.1350,224.9952,52,558820),(104.877,49.896,23632607,473.6387,225.3369,52,704657),(127.218,60.004,28739902,478.9694,225.9109,53,851449),(169.439,79.847,38296488,479.6237,226.9192,53,1110902),(189.226,89.432,42723806,477.7227,225.7823,53,1223050),(210.699,100.053,47493933,474.6894,225.4109,53,1333605)]
r=np.array(rows)
fig,ax=plt.subplots(figsize=(6.3,3.0))
ax.plot(r[:,0],r[:,3],'o-',label='ICR (wejściowa)',color='#1f5fa8',ms=4)
ax.plot(r[:,0],r[:,4],'s-',label='OCR (wyjściowa)',color='#c0392b',ms=4)
ax.set_xlabel('Czas rzeczywisty pomiaru [s]'); ax.set_ylabel('Częstość zliczeń [kcps]'); ax.set_ylim(0,550); ax.grid(alpha=.25)
ax2=ax.twinx(); ax2.plot(r[:,0],r[:,6]/r[:,1]/1e3,'^--',color='black',ms=4,label='kanał Al K$\\alpha$ 1,49 keV (średnia od startu)')
ax2.set_ylabel('Zliczenia w kanale 1,49 keV [10$^3$/s]',color='black'); ax2.set_ylim(0,18); import matplotlib.ticker as tk; ax2.yaxis.set_major_formatter(tk.FuncFormatter(lambda v,p: f'{v:g}'.replace('.',',')))
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels(); ax.legend(h1+h2,l1+l2,fontsize=8,loc='lower right')
fig.tight_layout(); fig.savefig(os.path.join(BASE,'stabilnosc_zliczen.pdf')); fig.savefig(os.path.join(BASE,'stabilnosc_zliczen.png'),dpi=200)
