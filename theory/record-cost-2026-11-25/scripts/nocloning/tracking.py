"""Route (c): tracking a continuously rotating phase theta(t)=theta0+omega t with a finite
system in continuous time.
(1) Proved in-model: a finite group (permutations of a simplex's vertices, D_n of a polygon)
has no non-trivial continuous one-parameter subgroup, so autonomous continuous-time change
on a finite reversible group must be stochastic jumps (Markov), i.e. irreversible.
(2) Ring Markov clock (n sites, forward k+, back k-): drift v=k+-k-, diffusion D=(k++k-)/2,
irreversibility rate sigma=(k+-k-)ln(k+/k-) (= KL rate between forward and time-reversed
path measures; an information quantity, no heat assumed). Angle variance after horizon tau:
V=(2pi/n)^2*2D*tau. Total irreversibility Sigma=sigma*tau. Closed form:
V*Sigma = Theta^2*(x+1)ln(x)/(x-1) >= 2 Theta^2, Theta=omega*tau, x=k+/k-; independent of n.
(3) Disk: rotation is in SO(2): reversible, zero irreversibility, error fixed at 1/2-1/pi.
(4) Cost comparison J = kappa*log2(N) + q*err + lam*Sigma, minimised over V for rings."""
import numpy as np
rng=np.random.default_rng(2)

print("(2) closed form check, simulated rings:")
for n,kp,km,tau in [(4,5.0,1.0,3.0),(12,40.0,30.0,2.0),(64,300.,290.,1.0)]:
    v=kp-km; omega=2*np.pi*v/n; Theta=omega*tau
    sig=(kp-km)*np.log(kp/km)
    nf=rng.poisson(kp*tau,400000); nb=rng.poisson(km*tau,400000)
    ang=(nf-nb)*2*np.pi/n; V=ang.var(); Sigma=sig*tau
    x=kp/km
    print(f"  n={n:3d} x={x:.3f}: V*Sigma/Theta^2 sim={V*Sigma/Theta**2:.4f} formula={(x+1)*np.log(x)/(x-1):.4f} (>=2)")

def err_ring(N,V,M=400):
    """later-question error for an N-bin classical (or N-vertex polygon used as bins) tracker
    whose angle estimate has quantisation (uniform within bin) plus Gaussian slip of variance V."""
    th=np.linspace(0,2*np.pi,M,endpoint=False); ph=th
    slip=rng.normal(0,np.sqrt(V),M) if V>0 else np.zeros(M)
    est=((np.floor(th/(2*np.pi/N))+0.5)*2*np.pi/N)[:,None]+slip[None,:]   # theta x samples
    tot=0
    for j,p in enumerate(ph[::8]):
        truth=np.cos(th-p)>0
        ans=np.cos(est-p)>0
        tot+=np.mean(ans!=truth[:,None])
    return tot/len(ph[::8])

disk_err=0.5-1/np.pi
Vs=[1e-3,1e-2,0.03,0.1,0.3,1,3,np.inf]
for q,lam in [(4.0,0.05),(4.0,0.005)]:
    print(f"\n(4) min J over V; kappa=1 per bit, q={q}, lam={lam} per nat; blind option J=q/2={q/2}")
    print("  Theta(rad) | best classical (N,V) J | square-bit ring J | disk J | cheapest")
    for Theta in [0,1,3,10,30,100]:
        opts={"blind":q*0.5}
        for N in [2,3,4,6,8,16]:
            for V in Vs:
                Sig=0 if (Theta==0 or V==np.inf) else 2*Theta**2/V
                Vt=0 if Theta==0 else V
                e=0.5 if Vt==np.inf else err_ring(N,Vt)
                J=np.log2(N)+q*e+lam*Sig
                k=f"classical N={N}"
                if J<opts.get(k,(9e9,))[0] if isinstance(opts.get(k),tuple) else True:
                    if k not in opts or J<opts[k][0]: opts[k]=(J,V)
        sq=min((1.0+q*(0.5 if (V==np.inf and Theta>0) else err_ring(4,0 if Theta==0 else V))+lam*(0 if (Theta==0 or V==np.inf) else 2*Theta**2/V)) for V in Vs)
        cl=min((v for k,v in opts.items() if k!="blind"),key=lambda t:t[0])
        clN=[k for k,v in opts.items() if v==cl][0]
        dj=1+q*disk_err
        allj={"blind":q/2,clN:cl[0],"square":sq,"disk":dj}
        print(f"  {Theta:6.0f} | {clN} V={cl[1]} J={cl[0]:.3f} | {sq:.3f} | {dj:.3f} | {min(allj,key=allj.get)}")
print("\n(5) many readers: R readers each get a fresh random later question.")
print("  disk with sequential projective reads (rebit Lueders rule) vs classical 1-bit record (copyable)")
M=1_000_000
for R in [1,2,3,5,10]:
    th=rng.uniform(0,2*np.pi,M); st=th.copy(); errs=[]
    for r in range(R):
        ph=rng.uniform(0,2*np.pi,M)
        plus=rng.random(M)<(1+np.cos(st-ph))/2
        errs.append(np.mean(plus!=(np.cos(th-ph)>0)))
        st=np.where(plus,ph,ph+np.pi)
    print(f"  R={R:2d}: disk mean error/reader={np.mean(errs):.4f} (first {errs[0]:.4f}, last {errs[-1]:.4f}); classical 1-bit copyable record=0.2500 each")
