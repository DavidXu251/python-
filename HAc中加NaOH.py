
import joblib
memory=joblib.Memory(location='.')


import sympy
solve=memory.cache(sympy.solve)

H,OH,Na,Ac,HAc=sympy.symbols(
    'H,OH,Na,Ac,HAc')
x,Kw,KAc=sympy.symbols('x,Kw,KAc')

H,OH,Na,Ac,HAc=solve([
    sympy.Eq(Ac+HAc, 1),
    sympy.Eq(Na         , x),
    sympy.Eq(H-OH+Na-Ac, 0),
    sympy.Eq(H*OH    ,Kw),
    sympy.Eq(H*Ac/HAc,KAc),
    ], (H,OH,Na,Ac,HAc) )

print(H)





