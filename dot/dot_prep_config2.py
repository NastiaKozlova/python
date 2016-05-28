def dot_preps(direk, prot):
    import os
    src=direk+'prepscript'
    drt=direk+'prepscript2'
    inputfile=open(src,'r')
    outputfile=open(drt,'w')
    strline=inputfile.readline()
    n= 0
    while len(strline)>0:
        n=n+1
        if n==84 or n==85 or n==102 or n==103:
            outputfile.write('#'+strline)
        else:
            outputfile.write(strline)
        strline=inputfile.readline()
    inputfile.close()
    outputfile.close()