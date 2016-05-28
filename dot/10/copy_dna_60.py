def copy_dna_60(direk,na,prot):
    import os,shutil
    #dna_name=direk+na+'/'
    dna_py=direk
    
    dna_out='/home/nastia/Desktop/python_ptograms/dna/dna_pdb/finish/'
    mdna=prot.upper()
    src=dna_out+mdna+'.pdb'
    dst=dna_py+na+'.pdb'
    shutil.copyfile(src, dst)
