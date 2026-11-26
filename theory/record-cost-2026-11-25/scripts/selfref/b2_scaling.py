"""B2: how uncopyable? Best linear copier error (least squares, max-abs entry over the orbit; metric is crude) vs
 (a) how well the tracker knows the drift (arc half-width delta) and (b) how far the target sits from the conserved axis (tilt theta)."""
import numpy as np
def hom(r): return np.concatenate([[1.0],np.asarray(r,float)])
def fit(states):
    W=np.array([hom(s) for s in states]).T; Y=np.array([np.kron(hom(s),hom(s)) for s in states]).T
    T,*_=np.linalg.lstsq(W.T,Y.T,rcond=None); return np.abs(T.T@W-Y).max()
def rotz(t): R=np.eye(3); R[:2,:2]=[[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]]; return R
print("(a) ball, target x+, drift about z known to +-delta (copier must work on the whole arc, 41 samples)")
ds=np.array([0.01,0.02,0.05,0.1,0.2,0.5,1.0]); es=[]
for d in ds:
    e=fit([rotz(t)@[1,0,0] for t in np.linspace(-d,d,41)]); es.append(e); print(f"   delta={d:5.2f}  err={e:.3e}")
sl=np.polyfit(np.log(ds[:4]),np.log(es[:4]),1)[0]; print(f"   small-delta scaling exponent ~ {sl:.2f}")
print("(b) ball, full drift orbit (latitude circle) of a state at tilt theta from the conserved axis")
th=np.array([0.01,0.02,0.05,0.1,0.2,0.4,0.8,np.pi/2]); es=[]
for t in th:
    e=fit([rotz(p)@[np.sin(t),0,np.cos(t)] for p in np.linspace(0,2*np.pi,48,endpoint=False)]); es.append(e)
    print(f"   theta={t:5.3f}  err={e:.3e}   sin^2(theta)/2={np.sin(t)**2/2:.3e}")
sl=np.polyfit(np.log(th[:4]),np.log(es[:4]),1)[0]; print(f"   small-theta scaling exponent ~ {sl:.2f}")
