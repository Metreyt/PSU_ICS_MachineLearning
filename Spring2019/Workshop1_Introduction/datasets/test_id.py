#!/usr/bin/env python
import id_fg
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import rdFMCS


#cmps = ['ethanol']
#cmps = ['ethanol','acetic acid','diethyl ether','acetone','acetic anhydride',
#        'ethyl acetate',"acetaldehyde", "propanal","cyclohexane",
#        'benzene', 'benzoic acid', 'phenol','benzaldehyde','isopentane','butane']
cmps = ['butane']

#results = pcp.get_substances('ethanol','name')
#print(results)

#cids = pcp.get_cids('ethanol','name')
#print(cids)

#c = pcp.Compound.from_cid(cids[0])

#structure = c.inchi
#print(structure)

for cmp in cmps:
    print(cmp)
    # We'll just grab the first cid
    cid = pcp.get_cids(cmp, 'name')[0]
    c = pcp.Compound.from_cid(cid)
    print(c.cid)
    pcp.download('PNG', 'images/'+cmp.replace(" ","_")+'.png', c.cid, 'cid',overwrite=True)
    m = Chem.MolFromInchi(c.inchi)
    #atoms_list = list(m.GetAtoms())
    #atoms = []
    #for i in range(len(atoms_list)):
    #    atoms.append(atoms_list[i])
    #print("Atoms: ", atoms)
    print("Alcohol: ",id_fg.is_alcohol(m))
    print("COOH: ", id_fg.is_cooh(m))
    print("Ketone: ", id_fg.is_ketone(m))
    print("Ether: ", id_fg.is_ether(m))
    print('Ester: ', id_fg.is_ester(m))
    print("Anhydride: ",id_fg.is_anhydride(m))
    print("Aldehyde: ", id_fg.is_aldehyde(m))
    print("Aromatic: ", id_fg.is_aromatic(m))
    print("Longest alphatic chain: ", id_fg.find_longest_alphatic_chain(m))
    print("------------------------------------")
        