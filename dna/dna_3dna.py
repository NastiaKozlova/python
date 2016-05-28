direk='/home/nastia/Desktop/python_ptograms/dna/dna_3dna/'
direkout='/home/nastia/Desktop/python_ptograms/dna/dna/'
import os
list_dna=os.listdir(direk)

for entry in list_dna:
    filein=open(direk+entry,'r')
    fileout=open(direkout+entry,'w')
    strline=filein.readline()
    strline=filein.readline()
    while len(strline)>4:
        fileout.write(strline[0:18]+'D'+strline[19:-1]+'\n')
        strline=filein.readline()
    filein.close()
    fileout.close()
