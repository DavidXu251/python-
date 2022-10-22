

pH_small=set('''H+ NH4+   Fe3+ Fe2+ Cu2+ Ba2+
'''.split() )

pH_large=set('''OH-  CO32-  SO32-
'''.split() )

special={
    {'Ba','SO4'},
    {'Ag','Cl'},
             }

print('判断共存模式')
while True:
    a=set( input('请输入可能存在的离子').split() )
    a_pH_small=a.instersection(pH_small)
    a_pH_large=a.instersection(pH_large)
    if len(a_pH_small)>0 and len(a_pH_large)>0:
        print('酸碱中和', a_pH_small, '和', a_pH_large)
    if 
