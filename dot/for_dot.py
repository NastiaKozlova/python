import os,shutil
#export DOT_ROOT=$HOME/dot2.0
#source $DOT_ROOT/bin/share/dot2.setup.bash

from dna import *
from dot_prep import *
from protein import *
from copy_dna import *
part_prot = '/home/nastia/Desktop/dot/'
list1 = os.listdir(part_prot)
#part=partname+ prot+'_'+dna+'/'+'coords/'
for prot in list1:
    list2= os.listdir(part_prot+prot)
    #print(part_prot+prot)
    for dna in list2:
        direk=part_prot+prot+'/'+dna+'/coords/'
        #print(direk)
        #print(direk)
        os.chdir (direk)
        #os.system ('ls')
        list3=os.listdir(direk)
        for entry in list3:
            na=''
            if entry.find('.')<4 and entry.find('.')>0:
                m=entry.find('.')
                na=entry[0:m]
                #print(na)
                #os.system ('gen_dot_prepscript -s '+prot+'.pdb -m '+ na+'.pdb -d 128 -l /home/nastia/test/data/uhbd.amber84.prot.dna.rlb')
                #os.system ('gen_dot_prepscript -s '+prot+'.pdb -m '+ dna+' -d 128 -l /home/nastia/test/data/uhbd.amber84.prot.dna.rlb')
                #os.system ('./prepscript 2>&1 |tee prepscript.log')
                #os.system ('pdb_make_centered '+direk+na+'/'+na+'.noh.pdb > '+direk+na+'/'+na+'.cen.noh.pdb')
                #shutil.copyfile(na+'/'+na+'.noh.cen.pdb', na+'/'+na+'.cen.noh.pdb')
                #os.system ('pdb_to_xyz '+direk+na+'/'+na+'.cen.noh.pdb > '+direk+na+'/'+na+'.cen.noh.xyz')
                #print(na, direk)
                #print(direk+'   '+na)
                #fdna(na, direk)
                #dot_prep(direk,prot)
                #os.system ('chmod +x prepscript1')
                #os.system ('./prepscript1 2>&1 |tee prepscript1.log')
                #dot_preps(direk, prot)
                #os.system ('chmod +x prepscript2')
                #os.system ('./prepscript2 2>&1 |tee prepscript2.log')
                #os.chdir (direk[0:-7])
                #print(direk[0:-7])
                #copy_dna(direk,na)
                makaka=dna+' '
                l=makaka.find('_')
                name=makaka[0:l]+makaka[l+1:-1]+'.deg06.nb0.parm'
                print(name)
                os.system('rundot '+ name)

            