
#export DOT_ROOT=$HOME/dot2.0
#source $DOT_ROOT/bin/share/dot2.setup.bash
#cd /home/nastia/Desktop/dot/coords/
def dot_prep(direk, prot):
    import os
    from prot_dot import *
    src=direk+'prepscript'
    drt=direk+'prepscript1'
    inputfile=open(src,'r')
    outputfile=open(drt,'w')
    strline=inputfile.readline()
    n= 0
    while len(strline)>0:
        n=n+1
        #if n==84 or n==85 or n==102 or n==103:
        if n==84 or n==85:
            outputfile.write('#'+strline)
        elif n==102:
            t=prot_dot(direk,prot)
            print(prot)
            if not t==1:
                outputfile.write(strline[0:21]+'-r Nterm'+str(t)+' '+strline[21:-1]+'\n')
            else:
                outputfile.write(strline)
        else:
            outputfile.write(strline)
        strline=inputfile.readline()
    inputfile.close()
    outputfile.close()
