/home/nastia/Desktop/main_files/1.10.10/1.10.10.60.txt
import os
from copy_prot1 import *
#from dna import *
from dot_run import *
from dot_prep import *
from protein import *
#from copy_dna1 import *
#import shutil

#os.system('export DOT_ROOT=$HOME/dot2.0')
#os.system('source $DOT_ROOT/bin/share/dot2.setup.bash')
not_dot=open('/home/nastia/Desktop/protein_name/1.10.10.60.txt','r')
part_prot = '/home/nastia/Desktop/dot1/'
strline=not_dot.readline()

#print(list1)
#part=partname+ prot+'_'+dna+'/'+'coords/'
while len(strline)>0:
#for prot in list1:
    prot=strline[0:4]
    list2= os.listdir(part_prot+prot)
    if not prot=='1a5j':
        for dna in list2:
            direk=part_prot+prot+'/'+dna+'/coords/'
            ditec=part_prot+prot+'/'+dna+'/'
            os.chdir (direk)
            list3=os.listdir(direk)
            for entry in list3:
                na=''
                if entry.find('.')<4 and entry.find('.')>0:
                    m=entry.find('.')
                    na=entry[0:m]
                #mas=(direk+na+'/')
                #os.system ('gen_dot_prepscript -s '+prot+'.pdb -m '+ na+'.pdb -d 128 -l /home/nastia/test/data/uhbd.amber84.prot.dna.rlb')
                #dot_prep(direk,prot)
                #mana=0
                #copy_prot(direk,prot)
                    os.system ('chmod +x prepscript1')
                    os.system ('./prepscript1 2>&1 |tee prepscript1.log')
                    #dot_preps(direk, prot)
                    #os.system ('chmod +x prepscript2')
                    #os.system ('./prepscript2 2>&1 |tee prepscript2.log')
                #print(ditec+prot+na+'.deg06.nb0.parm')
                    dot_run(ditec,prot,dna,na)
                 #   not_dot.write(lol)
    strline=not_dot.readline()
#not_dot.close()