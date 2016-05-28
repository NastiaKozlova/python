input_fine=open('/home/nastia/fine.60.txt','r')
input_fasta=open('/home/nastia/Desktop/fasta_end.txt','r')
output=open('/home/nastia/fasta_end.txt','w')
list_fasta=[]
strline=input_fasta.readline()
while len(strline)>0:
    list_fasta.append(strline)
    strline=input_fasta.readline()
input_fasta.close()
strline=input_fine.readline()
while len(strline)>0:
    dna=strline[0:4]
    mam=dna.upper()
    print(mam)
    s='aaggaaaggaaaggaaagga'
    m=s.upper()
    for entry in list_fasta:
        if (entry[0:4]==strline[0:4]) or mam==entry[0:4]:
            output.write(entry[0:-1]+'\t'+m+'\n')
    strline=input_fine.readline()
input_fine.close()
output.close()
    