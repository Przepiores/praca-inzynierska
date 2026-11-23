import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10,'axes.formatter.use_locale':False})
d=np.loadtxt('spektrum_dig.csv',delimiter=',',skiprows=1); E,C=d[:,0],d[:,1]
fig,ax=plt.subplots(figsize=(6.3,3.4))
ax.plot(E,C/1e3,color='#1f5fa8',lw=1.1)
lab=[(1.254,'Mg K$\\alpha$\n1,254'),(1.486,'Al K$\\alpha$\n1,486'),(1.740,'Si K$\\alpha$\n1,740')]
for e,t in lab:
    y=np.interp(e,E,C)/1e3; ax.annotate(t,(e,y),xytext=(0,6),textcoords='offset points',ha='center',fontsize=8)
ax.set_xlim(0,6); ax.set_ylim(0,1500)
ax.set_xlabel('Energia fotonu $E$ [keV]'); ax.set_ylabel('Liczba zliczeń [10$^3$ / 10 eV]')
ax.axvline(4.0,color='gray',ls='--',lw=0.8); ax.text(4.05,1250,'$eU_\\mathrm{T}$ = 4 keV\n(granica Duane’a–Hunta)',fontsize=8,color='gray')
ins=ax.inset_axes([0.55,0.38,0.42,0.3])
m=(E>2.2)&(E<4.6); ins.plot(E[m],C[m]/1e3,color='#1f5fa8',lw=0.9)
for e,t,yy,ha in [(2.972,'2·Al',35,'right'),(3.226,'Al+Si',31,'center'),(3.480,'2·Si',35,'left')]:
    ins.axvline(e,color='#c0392b',lw=0.6,ls=':'); ins.text(e,yy,t,fontsize=6.5,ha=ha,color='#c0392b')
ins.set_ylim(0,40); ins.tick_params(labelsize=7); ins.set_title('powiększenie 2,2–4,6 keV: piki sumacyjne',fontsize=7)
ax.grid(alpha=0.25)
def comma(ax_):
    import matplotlib.ticker as tk
    ax_.xaxis.set_major_formatter(tk.FuncFormatter(lambda v,p: f'{v:g}'.replace('.',',')))
comma(ax); comma(ins)
import matplotlib.ticker as tk
ins.yaxis.set_major_formatter(tk.FuncFormatter(lambda v,p: f'{v:g}'))
fig.tight_layout(); fig.savefig('/mnt/project-files/widma-eds/widmo_eds_4kV.pdf'); fig.savefig('/mnt/project-files/widma-eds/widmo_eds_4kV.png',dpi=200)

# wykres stabilności zliczeń: skrypty/stabilnosc.py
