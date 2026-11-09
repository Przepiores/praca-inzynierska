import numpy as np,glob,os
from PIL import Image
OUT='out'
def load(f): return np.asarray(Image.open(f).convert('RGB')).astype(float)
def metrics(a):
    R,G,B=a[...,0],a[...,1],a[...,2]
    ex=np.clip(B-np.maximum(R,G),0,None); m=ex>40
    area=int(m.sum()); H,W=B.shape
    if area==0: return dict(area=0,I=0,core=0,cf=0,r50=0,r90=0,cx=np.nan,cy=np.nan)
    ys,xs=np.nonzero(m); w=ex[m]
    cy,cx=np.average(ys,weights=w),np.average(xs,weights=w)
    r=np.hypot(ys-cy,xs-cx); o=np.argsort(r); c=np.cumsum(w[o])/w.sum()
    r50=r[o][np.searchsorted(c,.5)]; r90=r[o][np.searchsorted(c,.9)]
    core=int(((B>=250)&m).sum())
    d=np.hypot(H,W)
    return dict(area=area/(H*W)*100,I=w.sum()/(H*W),core=core/(H*W)*100,cf=core/area if area else 0,r50=r50/d*100,r90=r90/d*100,cx=cx,cy=cy)
# sessions: (file, label value, param)
S={
 'mg':[('mg/Sheet1_%02d'%i) for i in range(12)],
 's1':['b1/Sheet1_%02d'%i for i in [0,2,3,4,5]],
 's2':['b1/Sheet2_%02d'%i for i in range(10)],
}
lab={'mg':{0:'500',1:'600',5:'1000',9:'1400',11:'1600'},
     's1':{2:'800',4:'1000',5:'1100'},
     's2':dict(enumerate(['1','8','33','44.4','120','144','170','232','300','400']))}
res={}
for k,lst in S.items():
    rows=[]
    for i,p in enumerate(lst):
        f=glob.glob('imgs/'+p+'_r*.png')[0]; a=load(f); mt=metrics(a); mt['f']=f; rows.append(mt)
    res[k]=rows
    idx_map={'s1':[0,2,3,4,5]}.get(k,list(range(len(lst))))
    with open(f'{OUT}/dane/{k}.csv','w') as fh:
        fh.write('krok,etykieta,pole,I,rdzen,frakcja,r50,r90\n')
        for j,(i,mt) in enumerate(zip(idx_map,rows)):
            fh.write(f"{j+1},{lab[k].get(i,'nan')},{mt['area']:.3f},{mt['I']:.3f},{mt['core']:.3f},{mt['cf']:.3f},{mt['r50']:.3f},{mt['r90']:.3f}\n")
    print(open(f'{OUT}/dane/{k}.csv').read())
# crops
def crop(f,cx,cy,side,name):
    im=Image.open(f).convert('RGB'); h=side//2
    im.crop((int(cx-h),int(cy-h),int(cx+h),int(cy+h))).resize((600,600),Image.LANCZOS).save(f'{OUT}/figures/{name}.jpg',quality=90)
cen={}
for k in res:
    c=[(r['cx'],r['cy']) for r in res[k] if r['area']>0.3]
    cen[k]=np.nanmedian(np.array(c),axis=0)
print(cen)
side={'mg':520,'s1':460,'s2':520}
for k,lst in S.items():
    for p,r in zip(lst,res[k]):
        crop(r['f'],*cen[k],side[k],f"{k}_{os.path.basename(p)[-2:]}")
# full frames for reference
for k,p in [('mg','mg/Sheet1_09'),('s1','b1/Sheet1_05'),('s2','b1/Sheet2_09')]:
    f=glob.glob('imgs/'+p+'_r*.png')[0]; im=Image.open(f).convert('RGB'); im.thumbnail((1200,1200)); im.save(f'{OUT}/figures/{k}_pelny.jpg',quality=88)
