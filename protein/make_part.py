#!/usr/bin/python
import os, shutil
part = '/home/nastia/Desktop/HomeoDomain/protein/'
partout = '/home/nastia/Desktop/protein/'
part1 = part+'pdb/'
part2 =part+ 'out/'
part3 =part +'fasta/'
part4=part+'nucleus/'
list1 = os.listdir(part1)
#list2 = os.listdir(part2)
for entry in list1:
    pdbid = entry[0:4]
    partname = partout + pdbid +'/' 
    if not os.path.exists(partname):
        os.makedirs(partname+ 'pdb/')
        os.makedirs(partname+ 'out/')
        os.makedirs(partname+ 'fasta/')
        os.makedirs(partname+ 'nucleus')
        dst1 = partname + 'pdb/'+pdbid + '.pdb'
        src1 = part1+ entry
        dst2 = partname + 'out/'+pdbid + '.pdb'
        src2 = part2 + entry
        dst3 = partname + 'fasta/'+pdbid + '.fasta'
        src3 = part3 + pdbid+'.fasta'
        dst4 = partname+ 'nucleus/n'+pdbid + '.pdb'
        src4 = part4 +'n' +pdbid+'.pdb'
        shutil.copyfile(src1, dst1)
        shutil.copyfile(src2, dst2)
        #if os.path.exists(src3): 
        shutil.copyfile(src3, dst3)
        shutil.copyfile(src4, dst4)
        #else:
         #   print(src3)
    print(pdbid)
print('done')