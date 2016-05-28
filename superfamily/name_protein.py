import os
from dif_copy_part import *
lis='/home/nastia/Desktop/main_files/1.10.10/'
list_ma=os.listdir(lis)
for entry in list_ma:
    protein_part='/home/nastia/Desktop/main_files/1.10.10/'+entry
    tes='/home/nastia/Desktop/protein/'+entry
    protein=open(protein_part,'r')
    strline=protein.readline()
    output=open('/home/nastia/Desktop/protein_name/'+entry,'w')
    while len(strline)>0:
        pdb='/home/nastia/Desktop/dot1/'+strline[0:4]+'/'+strline[0:4]+'_1'+'/coords/'+strline[0:4]+'.pdb'
        if os.path.isfile(pdb):
            protein_pdb=open(pdb,'r')
            str_pdb=protein_pdb.readline()
            output.write(strline[0:4])
            while len(str_pdb)>0:
                if str_pdb.find('TITLE')>-1:
                    output.write('\t'+str_pdb[9:-1])
                if str_pdb.find('KEYWDS')>-1:
                    output.write('\t'+str_pdb[9:-1])
                if str_pdb.find('EXPDTA')>-1:
                    output.write('\t'+str_pdb[9:-1])
                str_pdb=protein_pdb.readline()
                output.write('\n')
            protein_pdb.close()
        strline=protein.readline()
    output.close()
    protein.close()
    input1=open('/home/nastia/Desktop/protein_name/'+entry,'r')
    listm = []
    str1 = input1.readline()
    while len(str1)>0:
        listm.append(str1)
        str1 = input1.readline()
    input1.close()
    output=open(tes,'w')
    listm.sort()
    lastsdr = ''
    for entry in listm:
        if len(entry)>2:
            if lastsdr == entry: 
                lastsdr = entry
            else:
                output.write(entry)
                lastsdr = entry
    output.close()
    output=open(tes,'r')
    strline=output.readline()
    while len(strline)>0:
        dir1='/home/nastia/Desktop/dot1/'+strline[0:4]+'/'+strline[0:4]+'_1'+'/coords/'+strline[0:4]
        dir2='/home/nastia/Desktop/dot_60/'+tes[29:-4]+'/'+strline[0:4]+'/'+strline[0:4]+'_1'+'/coords/'+strline[0:4]
        print(dir2)
        copy_dir(dir1, dir2)
        strline=output.readline()

