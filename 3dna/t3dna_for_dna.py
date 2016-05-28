def t3dna (partin, partout): 
    import os
    list = os.listdir(partin)
    outfile =partin[0:-1]+'.txt'
    
    output = open(outfile, 'w')
    for entry in list:	
        pdbid=entry[1:-4]
        filename = partin + entry 
        filenameout = partout + entry
        if os.path.getsize(filename)>0 and not partout==filename:
            os.system('/home/nastia/Desktop/python_ptograms/3dna/x3dna-dssr --input=' +filename +' --output=' +filenameout + '.out')
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