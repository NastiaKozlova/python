#!/usr/bin/python
import os, shutil
part_prot = '/home/nastia/Doco/protein_pdb/'
part_dna ='/home/nastia/Desktop/dna/'
partout = '/home/nastia/Desktop/dot_60/1.10.10.60/'
list2 = os.listdir(part_dna)
list1 = os.listdir(part_prot)
for prot in list1:
    pdbid = prot[0:4]
    partname = partout + pdbid +'/' 
    os.makedirs(partname+ '/')
    #if not os.path.exists(partname):
    part=partname+ pdbid+'_1/'+'/'+'coords/'
    #    os.makedirs(part)
    dst_prot = part+'/'+prot
    src_prot = part_prot+prot
    #    dst_dna = part+dna
     #   src_dna = part_dna + dna
        #    print(src_prot)
    shutil.copyfile(src_prot, dst_prot)
    #    shutil.copyfile(src_dna, dst_dna)
    print(pdbid)
print('done')