#!/usr/bin/python
import os, shutil
part_prot = '/home/nastia/Desktop/HomeoDomain/protein/out/'
part_dna ='/home/nastia/Desktop/dna/'
partout = '/home/nastia/Desktop/dot1/'
part_dna_dot='/home/nastia/Desktop/dna_dot/'
list2 = os.listdir(part_dna)
list1 = os.listdir(part_prot)
for prot in list1:
    pdbid = prot[0:4]
    partname = partout + pdbid +'/' 
    #os.makedirs(partname+ '/')
    #if not os.path.exists(partname):
    for dna in list2:
        list_dna_dot=[]
        part=partname+ pdbid+'_'+dna[0:-4]+'/'+'coords/'
        #os.makedirs(part)
        dst_prot = part+'/'+prot
        src_prot = part_prot+prot
        dst_dna = part+dna
        src_dna = part_dna + dna
        dna_dot=part_dna_dot+dna[0:-4]+'/'
        list_dna_dot=os.listdir(dna_dot)
        
        #print(list_dna_dot)
        for entry in list_dna_dot:
            shutil.copyfile(dna_dot+entry,part +dna[0:-4]+'/'+dna)
            
        #shutil.copyfile(src_prot, dst_prot)
        #shutil.copyfile(src_dna, dst_dna)
    #print(pdbid)
#print('done')