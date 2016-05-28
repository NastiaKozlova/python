def dot_run(ditec,prot,dna,na):
    import os
    if os.path.exists(ditec+prot+na+'.deg06.nb0.parm'):
        exit=open(ditec+dna+'.bash','w')
        exit.write('#!/bin/bash\n')
        exit.write('export DOT_ROOT=$HOME/dot2.0\n')
        exit.write('source $DOT_ROOT/bin/share/dot2.setup.bash\n')
        exit.write('cd '+ditec+'\n')
        exit.write('rundot '+ prot+na+'.deg06.nb0.parm\n')
        exit.write('python /home/nastia/Desktop/python_ptograms/dot/60/make_fin.py')
        exit.close()
        os.system ('chmod +x '+ditec+dna+'.bash')
        os.system('xfce4-terminal --command="'+ditec+dna+'.bash'+'"')