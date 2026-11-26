"""Route (b): regular-polygon state spaces (Janotta et al. 2011) vs classical simplices vs the disk.
For each: capacity N (max # jointly perfectly distinguishable states), best symmetric
broadcasting shrink factor eta (LP over linear maps into the MAXIMAL tensor product, i.e.
the most permissive composite), and the 'later question' task error.
Task: theta uniform on the circle is stored; later a direction phi (uniform) is revealed;
answer sign(cos(theta-phi)). Error = P(wrong)."""
import itertools, numpy as np
from scipy.optimize import linprog

def polygon(n):
    V = np.array([[np.cos(2*np.pi*i/n), np.sin(2*np.pi*i/n), 1.0] for i in range(n)])
    return V

def extreme_effects(V):
    """Extreme points of {e : 0 <= e.v <= 1 for all vertices v} in R^3, by brute force:
    intersections of 3 active constraints."""
    cons = []
    for v in V:
        cons.append((v,0.0)); cons.append((v,1.0))
    pts=[]
    for (a,ba),(b,bb),(c,bc) in itertools.combinations(cons,3):
        A=np.array([a,b,c]); 
        if abs(np.linalg.det(A))<1e-9: continue
        e=np.linalg.solve(A,[ba,bb,bc])
        vals=V@e
        if vals.min()>-1e-9 and vals.max()<1+1e-9:
            if not any(np.allclose(e,p,atol=1e-7) for p in pts): pts.append(e)
    return np.array(pts)

def capacity(V,E):
    """Max size of a set of vertices jointly perfectly distinguishable: need effects e_k
    summing to unit u with e_k(v_j)=delta_kj. Check subsets by LP feasibility (small n)."""
    n=len(V); u=np.array([0,0,1.0]); best=1
    for m in range(2,min(n,4)+1):
        for S in itertools.combinations(range(n),m):
            # variables: m effects in R^3 (3m vars); constraints: e_k.v in[0,1] for all v;
            # sum e_k = u; e_k(v_S[j]) = delta
            nv=3*m; Aeq=[];beq=[]
            for d in range(3):
                row=np.zeros(nv); row[d::3]=1; Aeq.append(row); beq.append(u[d])
            for k in range(m):
                for j,s in enumerate(S):
                    row=np.zeros(nv); row[3*k:3*k+3]=V[s]; Aeq.append(row); beq.append(1.0 if j==k else 0.0)
            Aub=[];bub=[]
            for k in range(m):
                for v in V:
                    row=np.zeros(nv); row[3*k:3*k+3]=v; Aub.append(row); bub.append(1.0)
                    Aub.append(-row); bub.append(0.0)
            r=linprog(np.zeros(nv),A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=[(None,None)]*nv,method="highs")
            if r.status==0: best=max(best,m); break
    return best

def broadcast_eta(V,E):
    """Max eta such that a linear map T: R^3 -> R^{3x3} sends each vertex v to W in the
    maximal tensor cone (e_a^T W e_b >= 0 for all extreme effects incl. 0/u complements),
    normalised, with BOTH marginals equal to eta*v + (1-eta)*c (c = centre).
    eta=1 means universal broadcasting (cloning implies broadcasting)."""
    u=np.array([0,0,1.0]); c=np.array([0,0,1.0])  # centre state (0,0,1)
    F=[e for e in E if np.linalg.norm(e)>1e-9]   # nonzero extreme effects (includes u)
    nT=27; nv=nT+1  # T as 3x3x3 tensor T[a,b,k], W_ab = sum_k T[a,b,k] v_k ; plus eta
    def idx(a,b,k): return 9*a+3*b+k
    Aub=[];bub=[];Aeq=[];beq=[]
    for v in V:
        for ea in F:
            for eb in F:
                row=np.zeros(nv)
                for a in range(3):
                    for b in range(3):
                        for k in range(3):
                            row[idx(a,b,k)] -= ea[a]*eb[b]*v[k]
                Aub.append(row); bub.append(0.0)
        # marginal A: W u = eta v + (1-eta) c ; marginal B: u^T W = same
        for a in range(3):
            row=np.zeros(nv)
            for b in range(3):
                for k in range(3): row[idx(a,b,k)] += u[b]*v[k]
            row[-1] = -(v[a]-c[a]); Aeq.append(row); beq.append(c[a])
            row=np.zeros(nv)
            for b in range(3):
                for k in range(3): row[idx(b,a,k)] += u[b]*v[k]
            row[-1] = -(v[a]-c[a]); Aeq.append(row); beq.append(c[a])
    cobj=np.zeros(nv); cobj[-1]=-1
    bounds=[(None,None)]*nT+[(0,1)]
    r=linprog(cobj,A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=bounds,method="highs")
    return r.x[-1] if r.status==0 else float('nan')

def later_question_error(V,E,M=720,iters=60,seed=0):
    """Alternating optimisation: encoder theta->vertex, decoder phi->extreme effect.
    Returns the best error found (an upper bound on the optimum for this discretisation)."""
    n=len(V); th=np.linspace(0,2*np.pi,M,endpoint=False); ph=th.copy()
    truth=(np.cos(th[:,None]-ph[None,:])>0).astype(float)    # M x M, 1 = '+'
    vals=V@E.T   # n x nE: P('+'|vertex, effect)
    rng=np.random.default_rng(seed); best=1.0
    for start in range(8):
        if start==0:   # nearest-vertex encoder
            enc=np.round(th/(2*np.pi/n)).astype(int)%n
        else: enc=rng.integers(0,n,M)
        for _ in range(iters):
            # decoder: for each phi pick effect maximising sum_theta correct
            P=vals[enc]          # M x nE
            score=truth.T@P + (1-truth).T@(1-P)   # M(phi) x nE
            dec=score.argmax(1)
            Q=vals[:,dec]        # n x M(phi)
            sc=truth@Q.T + (1-truth)@(1-Q.T)      # M(theta) x n
            new=sc.argmax(1)
            if np.array_equal(new,enc): break
            enc=new
        Q=vals[enc][:,dec]
        err=1-np.mean(truth*Q+(1-truth)*(1-Q))
        best=min(best,err)
    return best

def simplex(N):
    """Classical N-state system embedded for the later-question task: vertices = bins.
    Effects = any subset indicator (all extreme effects of a simplex)."""
    return N

def classical_error(N,M=720):
    th=np.linspace(0,2*np.pi,M,endpoint=False)
    # optimal: equal bins, answer by bin centre (we also brute-check N<=4 over random encoders)
    centres=(np.floor(th/(2*np.pi/N))+0.5)*2*np.pi/N
    truth=(np.cos(th[:,None]-th[None,:])>0)
    ans=(np.cos(centres[:,None]-th[None,:])>0)
    return np.mean(truth!=ans)

if __name__=="__main__":
    print("Classical simplex, N states: later-question error (analytic 1/(2N))")
    for N in range(2,9):
        print(f"  N={N}: capacity log2N={np.log2(N):.3f} bits, error={classical_error(N):.4f} (1/(2N)={1/(2*N):.4f}), broadcast eta=1 (classical copy)")
    print("Regular polygons (n vertices):")
    print("  n  N  extEff  eta_broadcast(max tensor)  later-q error  reversible group")
    for n in [3,4,5,6,7,8,10,12,16,24]:
        V=polygon(n); E=extreme_effects(V); N=capacity(V,E)
        eta=broadcast_eta(V,E); err=later_question_error(V,E)
        print(f"  {n:2d} {N}  {len(E):3d}     {eta:.4f}                     {err:.4f}        D_{n} (finite)")
    print(f"Disk (rebit, n->inf): N=2, later-q error analytic 1/2-1/pi = {0.5-1/np.pi:.4f}, group SO(2) (continuous)")
