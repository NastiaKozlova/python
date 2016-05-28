import os,shutil 
#from dif_copy_part import *
lis='/home/nastia/Desktop/main_files/1.10.10/'
list_ma=os.listdir(lis)
#os.makedirs('/home/nastia/Desktop/protein_name/')
test_fin='/home/nastia/Desktop/protein/'
test='/home/nastia/Desktop/protein_name/'
pdb_locate='/home/nastia/Desktop/protein_pdb/'
for entry in list_ma:
    print(entry)
    protein_part=lis+entry
    tes=test_fin+entry
    protein=open(protein_part,'r')
    strline=protein.readline()
    
    output=open(test+entry,'w')
    while len(strline)>0:
        if not os.path.exists('/home/nastia/Desktop/dot_60/'+entry[0:-4]+'/'+strline[0:4]):
            os.makedirs('/home/nastia/Desktop/dot_60/'+entry[0:-4]+'/'+strline[0:4])
        pdb=pdb_locate+strline[0:4]+'.pdb'
        if os.path.isfile(pdb):
            protein_pdb=open(pdb,'r')
            str_pdb=protein_pdb.readline()
            output.write(strline[0:4])
            #print(strline[0:4])
            while len(str_pdb)>0:
                if str_pdb.find('TITLE')==0:
                    output.write('\t'+str_pdb[9:-1])
                if str_pdb.find('KEYWDS')==0:
                    output.write('\t'+str_pdb[9:-1])
                if str_pdb.find('EXPDTA')==0:
                    output.write('\t'+str_pdb[9:-1])
                if str_pdb.find('DBREF')==0 and str_pdb.find('UNP')>0:
                    output.write('\t'+str_pdb[0:-1])
                str_pdb=protein_pdb.readline()
            protein_pdb.close()
            output.write('\n')
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
    #output=open(tes,'r')
    #strline=output.readline()
    #while len(strline)>0:
        #prot=strline[0:4]
        #dir1='/home/nastia/Desktop/protein_vmd/'+prot+'.pdb'
        #dr='/home/nastia/Desktop/dot_60/'+tes[29:-4]+'/'+prot+'/'
        #if os.path.exists(dr):
            #print(dr)
            #os.makedirs(dr+prot+'_1'+'/coords/')
            
            #dir2=dr+prot+'_1'+'/coords/'+prot+'.pdb'
            #dir5=dr+prot+'_n'+'/coords/'+prot+'.pdb'
            #shutil.copyfile(dir1,dir2)
            
            #dna=prot.upper()
            #dir3='/home/nastia/Desktop/python_ptograms/dna/dna_pdb/finish/'+dna+'.pdb'
            #dir4=dr+prot+'_n'+'/coords/'+prot+'n.pdb'
            #dir6='/home/nastia/Desktop/python_ptograms/dna/dna_pdb_1/finish/1.pdb'
            #dir7=dr+prot+'_1'+'/coords/1.pdb'
            #if os.path.isfile(dir3):
                #os.makedirs(dr+prot+'_n'+'/coords/')
                #shutil.copyfile(dir3, dir4)
                ##shutil.copyfile(dir1, dir5)
            #shutil.copyfile(dir6, dir7)
        #strline=output.readline()
    #output.close()

