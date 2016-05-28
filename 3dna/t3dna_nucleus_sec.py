def t3dna (partout, part, pdbid): 
    import os
    #delete all in partout
    list = os.listdir(partout)
    #for entry in list:
        #os.remove(partout+ entry)	
    #run 3dna
    list = os.listdir(part)
    outfile =partout[0:-1]+'.txt'
    output = open(outfile, 'w')
    for entry in list:
        #print(entry)
        filename = part + entry 
        #filenameout = partout + entry
        print(filename)
        inputfile = open (filename, 'r')
        output.write("\n")
        output.write(pdbid+'\t')
        for i in range (30):
            strline = inputfile.readline()
        #print(strline)
        while len(strline)>2:
            if strline.find('List of') and strline.find('base pairs'):
                #print(strline)
                break
            else:
                strline = inputfile.readline()
        print(strline)
        strline = inputfile.readline()
        while len(strline)>2:
            output.write(strline[35])
            strline = inputfile.readline()
        inputfile.close()	
    output.close()