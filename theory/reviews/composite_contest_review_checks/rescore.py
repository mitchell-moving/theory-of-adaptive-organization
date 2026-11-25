import math
for lam in (1e-4,1e-3,1e-2,1e-1):
    jc=lam*math.log(16); jr=lam*math.log(10); tol=0.01*max(jc,jr)+1e-12
    print(f"lam {lam:g}: J_C {jc:.6g} J_R(L=0) {jr:.6g} delta {jr-jc:.3e} tol {tol:.3e} -> {'LOSE' if jr-jc<-tol else 'other'}")
# H1: 2-state classical record = sign of n
poles=[(s,i) for i in range(3) for s in (1,-1)]
err=0;scored=0
for s,i in poles:
    for u in range(3):
        if u!=i: continue
        scored+=1
        target=s; out_A=s; out_B=s   # each wing outputs the shared sign bit, whatever the query
        err+= (out_A!=target)+(out_B!=target)
print("H1 two-state record: scored pairs",scored,"errors",err,"; I(n;record)=ln2=",math.log(2),"vs Holevo of |n>|n> ensemble ln3=",math.log(3))
for lam in (1e-4,1e-1): print(f"H1 lam {lam:g}: J(M=2)={lam*math.log(2):.4g} J(prod K=4)={lam*math.log(4):.4g} J_C={lam*math.log(16):.4g}")
