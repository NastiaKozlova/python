filein=open('/home/nastia/Desktop/python_ptograms/dna/dna.txt','r')
fileout=open('/home/nastia/Desktop/python_ptograms/dna/dna_sec.txt','w')
strline=filein.readline()
n=0
while len(strline)>0:
    n=n+1
    #print(strline[0:-1])
    fileout.write(str(n)+'\t'+strline[0:-1]+'\n')
    strline=filein.readline()
filein.close()
fileout.close()