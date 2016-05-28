def copy_dna(direk,na):
    import os,shutil
    dna_name=direk+na+'/'
    #dna_py=mas
    dna_out='/home/nastia/Desktop/dna_dot/'+na+'/'
    print(dna_name)
    if not os.path.exists(dna_out):
        os.makedirs(dna_out)
        list_in=os.listdir(dna_name)
        for entry in list_in:
            src=dna_name+entry
            dst=dna_out+entry
            #print(src+'   '+dst)
            shutil.copyfile(src, dst)
   # dna_py=dna_name[0:24]+'1'+dna_name[24:-1]+'/'            
   #/home/nastia/Desktop/dot1/1a04/1a04_1    #os.system('cp '+dna_name+' '+dna_out)