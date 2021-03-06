#!/usr/bin/env python
import pandas as pd
import re
from rdkit import Chem

import id_fg

def mol_wt_CHO(form_dict):
    massC = 12.0107
    massH = 1.00794
    massO = 15.999
    mol_wt = float(form_dict['C'])*massC + float(form_dict['H'])*massH + float(form_dict['O'])*massO
    return mol_wt

def dou_CHO(form_dict):
    c = form_dict['C']
    h = form_dict['H']
    o = form_dict['O']
    dou = (2*int(c)+2-int(h))/2
    return dou

def get_inchi_from_smiles(smiles):
    m = Chem.MolFromSmiles(smiles)
    inchi = Chem.MolToInchi(m)
    return inchi

def get_chem_form_inchi(inchi):
    #InChI are strings like this
    #InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3
    # That is ethanol
    #All InChI start with InchI=
    # The next part is the version and standard number
    # After the / is the chemical formula
    # After the next next /c is the connectivity of the heavy atoms
    # Then after /h is the is the hydrogren connectivity.
    # There are additional layers as needed.
    inchi_string =  inchi.split('=')[-1]
    chem_form = inchi_string.split('/')[1]
    return chem_form

def split_chem_form(chem_form):
    set = re.findall(r'([A-Z][a-z]*)(\d*)', chem_form)
    form_dict = {}
    for element in set:
        if element[0] in form_dict.keys():
            count = '1'
            if element[1] != '':
                form_dict[element[0]] = int(form_dict[element[0]]) + int(element[1])
            else:
                form_dict[element[0]] = int(form_dict[element[0]]) + int(count)
        if element[0] not in form_dict.keys():
            count = '1'
            if element[1] != '':
                form_dict[element[0]] = element[1]
            else:
                form_dict[element[0]] = count
    return form_dict

def form_dict_only_CHO(form_dict):
    is_only_CHO = True
    for element in form_dict.keys():
        if element not in ['C','H','O']:
            is_only_CHO = False
    return is_only_CHO
    

df = pd.read_csv('ONSMeltingPoints.tsv',sep='\t')

#print(df)
print(df.columns)


output = open('filter_mp.tsv','w')
#output.write('csid\tmp\tinchi\tname\tc\th\to\tOH\tCO\tdou\tCHO\tCOOH\tROR\tCOOR\tAromatic\n')
output.write('csid\tmp\tinchi\tname\tc\th\to\tmol_wt\tdou\tAromatic\tOH\tCO\tCHO\tCOOH\tCOOR\tROR\n')
#print(df[['Ave','SMILES','name']].head())
#for i in range(len(df['SMILES'])):
for i in range(len(df['SMILES'])):
    try:
        smiles = df['SMILES'][i]
        mol = Chem.MolFromSmiles(smiles)
        alc = str(int(id_fg.is_alcohol(mol)))
        ket = str(int(id_fg.is_ketone(mol)))
        cho = str(int(id_fg.is_aldehyde(mol)))
        cooh = str(int(id_fg.is_cooh(mol)))
        ror = str(int(id_fg.is_ether(mol)))
        coor = str(int(id_fg.is_ester(mol)))
        aro = str(int(id_fg.is_aromatic(mol)))
        inchi = get_inchi_from_smiles(smiles)
        chem_form = get_chem_form_inchi(inchi)
        form_dict = split_chem_form(chem_form)
        is_only_CHO = form_dict_only_CHO(form_dict)
        if is_only_CHO:
            #print(i, smiles,inchi,  chem_form, form_dict)
            #print(df['CSID'][i])
#            output.write(str(df['CSID'][i])+'\t'+str(df['Ave'][i])+'\t'+inchi+
#                         '\t'+str(df['name'][i])+'\t'+form_dict['C']+
#                         '\t'+form_dict['H']+'\t'+form_dict['O']+
#                         '\t'+alc+'\t'+ket+'\t'+cho+'\t'+
#                         '\t'+cooh+'\t'+ror+'\t'+coor+'\t'+aro+'\n')
            dou = dou_CHO(form_dict)
            mol_wt = mol_wt_CHO(form_dict)
            output.write('csid'+str(df['CSID'][i])+'\t'+str(df['Ave'][i])+'\t'+inchi+
                         '\t'+str(df['name'][i])+'\t'+form_dict['C']+
                         '\t'+form_dict['H']+'\t'+form_dict['O']+
                         '\t'+str(mol_wt)+'\t'+str(dou)+
                         '\t'+aro+'\t'+alc+'\t'+ket+
                         '\t'+cho+'\t'+cooh+'\t'+coor+
                         '\t'+ror+'\n')
    except:
        continue
#    #inp = input('Continue [Y/n]')
#    #if inp == 'n':
#    #    break
output.close()
