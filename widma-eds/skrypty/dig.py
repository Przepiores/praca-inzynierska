import numpy as np
from PIL import Image
im=np.asarray(Image.open('/root/.claude/uploads/5da0df3b-6643-51d4-83fc-dae189acf4d4/fa87e5a2-image.jpg').convert('RGB')).astype(int)
H,W,_=im.shape
dark=(im.sum(2)<150)
def bottom(x):
    col=dark[850:1100,x]; idx=np.where(col)[0]; return 850+idx.max()
ticks={0:434,0.5:506,1:576,1.5:646,2:716,2.5:780,3:851,8.5:1550,9:1611,9.5:1671,10:1730,10.5:1789,11:1846,11.5:1904}
src=[];dst=[]
for e,x in ticks.items(): src.append((e,0)); dst.append((x,1034 if e==0 else bottom(x)))
for c,(x,y) in {0:(433,1036),1e5:(432,992),1.3e6:(420,447),1.4e6:(419,402)}.items(): src.append((0,c/1e5)); dst.append((x,y))
src.append((1.49,13.33605)); dst.append((630,431))
print(dst[:3],dst[-8:])
src=np.array(src,float); dst=np.array(dst,float)
A=[]
for (X,Y),(u,v) in zip(src,dst):
    A.append([X,Y,1,0,0,0,-u*X,-u*Y,-u]); A.append([0,0,0,X,Y,1,-v*X,-v*Y,-v])
_,_,Vt=np.linalg.svd(np.array(A)); Hm=Vt[-1].reshape(3,3)
def f(X,Y):
    p=Hm@np.array([X,Y,1.]); return p[:2]/p[2]
res=[np.hypot(*(f(*s)-d)) for s,d in zip(src,dst)]; print('resid px',np.round(res,1))
Hi=np.linalg.inv(Hm)
g=(im[:,:,1]>130)&(im[:,:,1]>im[:,:,0]+30)&(im[:,:,1]>im[:,:,2]+60)
ys,xs=np.where(g[360:1050,420:1960]); ys+=360; xs+=420
P=Hi@np.vstack([xs,ys,np.ones_like(xs)]); E=P[0]/P[2]; C=P[1]/P[2]*1e5
m=(E>=0)&(E<=11.8)&(C>-3e4)&(C<1.45e6)
E,C=E[m],C[m]
bins=np.round(E/0.02)*0.02
out={}
for b,c in zip(bins,C): out[b]=max(out.get(b,-1e9),c)
ks=sorted(out); arr=np.array([[k,max(out[k],0)] for k in ks])
# fill full grid
grid=np.round(np.arange(0,11.8001,0.02),2)
vals=np.interp(grid,arr[:,0],arr[:,1])
# cursor line gap: replace 1.44-1.54 using known peak
np.savetxt('spektrum_dig.csv',np.c_[grid,vals],delimiter=',',fmt='%.3f',header='E_keV,counts',comments='')
for e in [0.8,1.0,1.1,1.2,1.25,1.3,1.4,1.45,1.49,1.52,1.6,1.7,1.74,1.8,2.0,2.5,2.9,3.0,3.3,3.5,4,5,8]:
    print(e, int(np.interp(e,grid,vals)))
