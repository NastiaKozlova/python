#copy_prot
def copy_prot(direk,prot):
    import os,shutil
    prot_name=direk+prot+'/'
    #dna_py=mas
    prot_out='/home/nastia/Desktop/prot_dot/'+prot+'/'
    #print(prot_name)
    list_in=os.listdir(prot_name)
    m=0
    for entry in list_in:
        m=m+1
        for entry in list_in:
            if m>1:
                src=prot_name+entry
                dst=prot_out+entry
                if not os.path.exists(prot_out):
                    os.makedirs(prot_out)
                    shutil.copyfile(src, dst)
   # dna_py=dna_name[0:24]+'1'+dna_name[24:-1]+'/'            
   #/home/nastia/Desktop/dot1/1a04/1a04_1    #os.system('cp '+dna_name+' '+dna_out)