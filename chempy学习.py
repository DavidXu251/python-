
import pubchempy as pcp

for compound in pcp.get_compounds('glucose', 'name'):
    print(compound.cid)
    print(compound.isomeric_smiles)

    
import pubchempy as pcp

results=pcp.get_compounds(
    'C9H7O3', 'molecular_formula')

for i in results:
    print(i.get_properties('name'))
