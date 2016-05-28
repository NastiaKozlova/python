import os
from dna import *
from dot_run import *
from dot_prep import *
#from protein import *
#from copy_dna_60 import *
#from grid_test import *
import shutil
from runs_dot_finish import *
#export DOT_ROOT=$HOME/dot2.0
#source $DOT_ROOT/bin/share/dot2.setup.bash
#python /home/nastia/Desktop/python_ptograms/dot/60/for_dot_60.py
nope=open('/home/nastia/Desktop/dot_60/1.10.10.60.txt','w')
part_prot = '/home/nastia/Desktop/dot_60/1.10.10.60/'
list1 = os.listdir(part_prot)
for prot in list1:
    direk=part_prot+prot+'/'+prot+'_n/coords/' 
    ditec=part_prot+prot+'/'+prot+'_n/'
    na=prot+'n'
    pna=direk+prot+'n.pdb'
    #if os.path.exists(direk) and not os.path.exists(ditec+'latest/pdb/'):
    if os.path.exists(direk) and os.path.exists(ditec+'latest/pdb/'):
        #print(prot)
        #os.chdir (direk)
        #os.system ('gen_dot_prepscript -s '+prot+'.pdb -m '+ na+'.pdb -d 128 -l /home/nastia/Desktop/python_ptograms/dot/60/uhbd.amber84.prot.dna.rlb')
        #os.system ('./prepscript 2>&1 |tee prepscript.log')
        #os.system ('pdb_make_centered '+direk+na+'/'+na+'.noh.pdb > '+direk+na+'/'+na+'.cen.noh.pdb')
        #shutil.copyfile(direk+na+'/'+na+'.noh.cen.pdb', direk+na+'/'+na+'.cen.noh.pdb')
        #os.system ('pdb_to_xyz '+direk+na+'/'+na+'.cen.noh.pdb > '+direk+na+'/'+na+'.cen.noh.xyz')
        #dot_prep(direk, prot)
        #os.system ('chmod +x prepscript1')
        #os.system ('./prepscript1 2>&1 |tee prepscript1.log')
        #os.chdir (ditec)
        ##dot_run(ditec,prot,na)
        make_fin(ditec,prot,na)
    else:
        nope.write(prot+'\n')
nope.close()