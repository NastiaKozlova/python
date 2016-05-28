def copy_runs_n(ditec,prot):
    nope='/home/nastia/'+ditec[28:-12]+'_1'
    from dif_copy_part import *
    import os
    din=ditec+'latest/'
    #print(nope)
    #os.makedirs(nope)
    if os.path.exists(din):
        dir1=din
        #print(dir1)
        dir2=nope+prot
        
        #print(dir2)
        copy_dir(dir1, dir2)