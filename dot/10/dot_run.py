def dot_run(ditec,prot,na):
    import os
    if os.path.exists(ditec+prot+na+'.deg06.nb0.parm'):
        exit=open(ditec+na+'.bash','w')
        exit.write('#!/bin/bash\n')
        exit.write('export DOT_ROOT=$HOME/dot2.0\n')
        exit.write('source $DOT_ROOT/bin/share/dot2.setup.bash\n')
        exit.write('cd '+ditec+'\n')
        exit.write('rundot '+ prot+na+'.deg06.nb0.parm\n')
        exit.close()
        os.system ('chmod +x '+ditec+na+'.bash')
        os.system('xfce4-terminal --command="'+ditec+na+'.bash'+'"')