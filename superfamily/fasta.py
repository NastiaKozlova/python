import os
fasta_dir='/home/nastia/Doco/fasta/'
list_fasta=os.listdir(fasta_dir)
output=open('/home/nastia/Doco/fasta.txt','w')
for entry in list_fasta:
    fasta=open(fasta_dir+entry,'r')
    strline=fasta.readline()
    #name=''
    while len(strline)>0:
        #if not strline.find('>')>-1:
        #    lin=len(strline)
        #    for i in range (lin):
        #        if strline[i]=='a' or strline[i]=='t' or strline[i]=='g' or strline[i]=='c' or strline[i]=='n':
        #            output.write(entry[0:-4]+'\t'+strline)
        #else:
        #    name=strline
        if strline.find('>')>-1:
            output.write('\n'+strline)
        else:
            output.write(strline[0:-1])
        strline=fasta.readline()
    fasta.close()
output.close()
inputfile=open('/home/nastia/Doco/fasta.txt','r')
output=open('/home/nastia/Doco/fasta_end.txt','w')
strline=inputfile.readline()
name=''
sec=''

while len(strline)>0:
    lic=0
    if strline.find('>')==-1:
        #print(strline)
        lin=len(strline)
        lic=0
        for i in range (lin-1):
            
            if not (strline[i]=='A' or strline[i]=='T' or strline[i]=='G' or strline[i]=='C' or strline[i]=='N '):
                lic=lic+1
          
    else:
        name=strline
        #print(str(lic)+'   '+strline)
            
    if lic==0:
        #print(strline)
        if strline.find('|PDBID|CHAIN|SEQUENCE')==-1:
            output.write(name[1:5]+'\t'+strline)
        
    strline=inputfile.readline()
output.close()
inputfile.close()
                    
