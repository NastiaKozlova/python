import os
output=open('/home/nastia/name_not.txt','w')
inputfile=open('/home/nastia/fine.60_not.txt','r')
entry=inputfile.readline()
while len(entry)>0:
    filein=open('/home/nastia/Desktop/protein/1.10.10.60.txt','r')
    strline=filein.readline()
    while len(strline)>0:
        if strline[0:4]==entry[0:4]:
            output.write(strline)
        strline=filein.readline()
    filein.close()
    entry=inputfile.readline()
output.close()