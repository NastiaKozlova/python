import os
list1=os.listdir('/home/nastia/pymol_n/')
output=open('/home/nastia/name.txt','w')
for entry in list1:
    filein=open('/home/nastia/Desktop/protein/1.10.10.60.txt','r')
    strline=filein.readline()
    while len(strline)>0:
        if strline[0:4]==entry[0:4]:
            output.write(strline)
        strline=filein.readline()
    filein.close()
output.close()