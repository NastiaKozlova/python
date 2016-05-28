import os
from def_3dna import *
partin = '/home/nastia/Desktop/protein/'
#part, protein is here
result = '/home/nastia/Desktop/3dna/3dna_pdb.txt'
listdir = os.listdir(partin)
for pdbid in listdir:
    part =partin + pdbid +'/'+'pdb/'
    partout = partin + pdbid + '/3dna' +'/pdb/'
    if os.path.exists(part):
        if not os.path.exists(partout):
            os.makedirs(partout)
        t3dna (partout, part, partin, pdbid)
        file = partout[0:-1]+'.txt'
        resiltsfile =open(result,'a')
        paradock = open (file,'r')
        str = paradock.readline()
        while len(str)>0:
            resiltsfile.write(str)
            str = paradock.readline()
        paradock.close()
    resiltsfile.close()