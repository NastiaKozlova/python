ina='/home/nastia/Desktop/python_ptograms/dna/dna/a.pdb'
inc='/home/nastia/Desktop/python_ptograms/dna/dna/c.pdb'
ing='/home/nastia/Desktop/python_ptograms/dna/dna/g.pdb'
int='/home/nastia/Desktop/python_ptograms/dna/dna/t.pdb'
input='/home/nastia/Desktop/python_ptograms/dna/dna_sec.txt'
file_a=open(ina,'r')

t=50
inp=open(input, 'r')
strsm=inp.readline()

while len(strsm)>0:
    
    q=strsm.find('\t')
    strs=strsm[q+1:-1]+'\n'
    p=len(strs)-1
    print('#'+strs+'#')

    out1='/home/nastia/Desktop/python_ptograms/dna/dna_pdb_1/'+strsm[0:q] +'1.pdb'
    out2='/home/nastia/Desktop/python_ptograms/dna/dna_pdb_1/'+strsm[0:q] +'2.pdb'
    out='/home/nastia/Desktop/python_ptograms/dna/dna_pdb_1/finish/'+strsm[0:q] +'.pdb'
    output1=open(out1,'w')
    output2=open(out2,'w')

    for i in range (p):
        bp=strs[i]
        
        m=i+1
        l=0
        f=0
    ##AAA
        if bp=='A' or bp=='a':
            input_a = open(ina, 'r')
            str_a=input_a.readline()
            while len(str_a)>0:
                sos=str_a[22:26]+'n'
                makaka=sos.rfind(' ')
                if sos[makaka+1:-1]==str(m):
                    output1.write(str_a)
                f=m+p
                l=m+t
                yf=len(str(f))
                yl=len(str(l))
                if sos[makaka+1:-1]==str(l):
                    output2.write(str_a[0:22]+sos[0:makaka+1]+(yl-yf)*' '+str(f)+str_a[26:-1]+'\n')
                str_a=input_a.readline()
            input_a.close()

	##CCC
        if bp=='c' or bp=='C':
            input_c = open(inc, 'r')
            str_c=input_c.readline()
            while len(str_c)>0:
                sos=str_c[22:26]+'n'
                makaka=sos.rfind(' ')
                if sos[makaka+1:-1]==str(m):
                    output1.write(str_c)
                f=m+p
                l=m+t
                yf=len(str(f))
                yl=len(str(l))
                if sos[makaka+1:-1]==str(l):
                    output2.write(str_c[0:22]+sos[0:makaka+1]+(yl-yf)*' '+str(f)+str_c[26:-1]+'\n')
                str_c=input_c.readline()
            input_c.close()

#   GGG
        if bp=='g'or bp=='G':
            input_g = open(ing, 'r')
            str_g=input_g.readline()
            while len(str_g)>0:
                sos=str_g[22:26]+'n'
                makaka=sos.rfind(' ')
                if sos[makaka+1:-1]==str(m):
                    output1.write(str_g)
                f=m+p
                l=m+t
                yf=len(str(f))
                yl=len(str(l))
                if sos[makaka+1:-1]==str(l):
                    output2.write(str_g[0:22]+sos[0:makaka+1]+(yl-yf)*' '+str(f)+str_g[26:-1]+'\n')
                str_g=input_g.readline()
            input_g.close()
            
	###TTT
        if bp=='t'or bp=='T':
            input_t = open(int, 'r')
            str_t=input_t.readline()
            while len(str_t)>0:
                sos=str_t[22:26]+'n'
                makaka=sos.rfind(' ')
                if sos[makaka+1:-1]==str(m):
                    output1.write(str_t)
                f=m+p
                l=m+t
                yf=len(str(f))
                yl=len(str(l))
                if sos[makaka+1:-1]==str(l):
                    output2.write(str_t[0:22]+sos[0:makaka+1]+(yl-yf)*' '+str(f)+str_t[26:-1]+'\n')
                str_t=input_t.readline()
            input_t.close()
    output1.close()
    output2.close()

    output1=open(out1,'r')
    output2=open(out2,'r')
    output=open(out,'w')
    output.write('REMARK    '+strs)
    strline = output1.readline()
    n=0
    while len(strline)>0:
        n=n+1
        yn=len(str(n))
     
        output.write(strline[0:4]+' '*(7-yn)+str(n)+strline[11:-1]+'\n')
        strline = output1.readline()
	
    #print(n)
    strline = output2.readline()
    while len(strline)>0:
        n=n+1
        yn=len(str(n))
        output.write(strline[0:4]+' '*(7-yn)+str(n)+strline[11:-1]+'\n')
        strline = output2.readline()  
    #print(n)
    output1.close()
    output2.close()
    output.close()

#	else:
#		print('not '+strs)
    strsm=inp.readline()
