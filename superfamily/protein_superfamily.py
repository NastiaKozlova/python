import os
from dif_copy_part import *
part='/home/nastia/Desktop/main_files/1.10.10/'
partin = '/home/nastia/Desktop/protein/'
partout ='/home/nastia/Desktop/superfamily/'
#test=open('/home/nastia/Desktop/test.txt','a')
list = os.listdir(part)
#print (list)
for entry in list:
    filename = part + entry 
    #print (entry)
    sf = open (filename, 'r')
    strline =sf.readline()
    while len(strline) > 0:
        st =strline[0:4]
        f=st
        dir1=partin+st
        dir2=partout+entry[0:-4]+'/'+st
        #test.write(dir1+'\t'+dir2+'\n')
        strline =sf.readline()
        if os.path.exists(dir1):
            #if not os.path.exists(dir2):
                #os.makedirs(dir2)
            copy_dir(dir1, dir2)
    sf.close()
#test.close()