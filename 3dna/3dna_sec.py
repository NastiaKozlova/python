import os
from t3dna_nucleus_sec import *
partin = '/home/nastia/Desktop/protein/'
#part, protein is here
result = '/home/nastia/Desktop/3dna/3dna_sec.txt'
listdir = os.listdir(partin)
for pdbid in listdir:
    part =partin + pdbid +'/3dna/nucleus/'
    filein=part+'n'+pdbid+'.pdb.out'
    partout = partin + pdbid + '/3dna/sec/'
    if os.path.exists(filein):
        #os.makedirs(partout)
        if not os.path.exists(partout):
            os.makedirs(partout)
        t3dna (partout, part, pdbid)
        file = partout[0:-1]+'.txt'
        resiltsfile =open(result,'a')
        paradock = open (file,'r')
        str = paradock.readline()
        while len(str)>0:
            resiltsfile.write(str)
            str = paradock.readline()
        paradock.close()
    resiltsfile.close()