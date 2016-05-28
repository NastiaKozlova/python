def t3dna (partout, part, partin,pdbid): 
    import os
    #delete all in partout
    list = os.listdir(partout)
    for entry in list:
        os.remove(partout+ entry)	
    #run 3dna
    list = os.listdir(part)
    outfile =partout[0:-1] +'.txt'
    output = open(outfile, 'w')
#    output.write('\npdbid\tname\tno. of DNA/RNA chains\tno. of nucleotides\tno. of atoms\tno. of waters\tno. of metals\n')
    for entry in list:	
        filename = part + entry 
        filenameout = partout + entry
        if filename.find('.pdb')>0:
            os.system('/home/nastia/Desktop/python_ptograms/paradock/paradock_test/x3dna-dssr --input=' +filename +' --output=' +filenameout + '.out')
            inputfile = open (filenameout + '.out', 'r')

            output.write("\n")
            output.write(pdbid+'\t')
            for i in range (23):	
                strline = inputfile.readline()	
            output.write(strline[11:-1] + "\t")	
            strline = inputfile.readline()	
            for i in range (5):	
                output.write(strline[27:-1] +'\t')	
                strline = inputfile.readline()	
            inputfile.close()	
    output.close()