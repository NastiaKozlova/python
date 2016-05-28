#!/usr/bin/python
import os, shutil
part_prot = '/home/nastia/Doco/protein_pdb/'
#part_dna ='/home/nastia/Desktop/python_ptograms/dna/dna_pdb/finish/'
partout = '/home/nastia/Desktop/dot_60/1.10.10.60/'

list1 = os.listdir(partout)
for prot in list1:
    dst = partout + prot +'/'+ prot+'_1/'+'coords/'+prot+'.pdb'
    src = part_prot+prot+'.pdb'
    print(dst +'  '+src)
    shutil.copyfile(src, dst)
     
    #print(pdbid)
#print('done')