import os
from def_3dna import *
partin = '/home/nastia/Desktop/protein/'
#part, protein is here
result = '/home/nastia/Desktop/3dna/3dna_nucleus.txt'
listdir = os.listdir(partin)
resiltsfile =open(result,'w')
for pdbid in listdir:
    part =partin + pdbid +'/'+'nucleus/'
    partout = partin + pdbid + '/3dna' +'/nucleus/'

    if os.path.exists(part):
        print('#'+partout)
        if not os.path.exists(partout):
            print('#'+part)
            os.makedirs(partout)
            
        if os.path.exists(partin+pdbid+'/nucleus/'+'n'+pdbid+'.pdb'):
            filet=open (partin+pdbid+'/nucleus/'+'n'+pdbid+'.pdb','r')
            x = filet.readline()
            if len(x)>0:
                filet.close()
                t3dna (partout, part, partin, pdbid)
                file = partout[0:-1]+'.txt'
                #resiltsfile =open(result,'a')
                paradock = open (file,'r')
                str = paradock.readline()
                while len(str)>0:
                    resiltsfile.write(str)
                    str = paradock.readline()
                paradock.close()
                #resiltsfile.close()
            else:
                #resiltsfile =open(result,'a')
                resiltsfile.write(pdbid+'\tno dna\n')
                #resiltsfile.close()
        else:
            #resiltsfile =open(result,'a')
            resiltsfile.write(pdbid+'\tno dna\n')
resiltsfile.close()