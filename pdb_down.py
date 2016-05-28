import os
stro='/home/nastia/Desktop/dot1/'
list1=os.listdir(stro)
pdb_down=open('/home/nastia/Desktop/pdb_down.txt','w')
for entry in list1:
    pdb_down.write(entry+', ')
pdb_down.close()