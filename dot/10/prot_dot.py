def prot_dot(direk,prot):
    m=direk.find('_')
    n=direk.rfind('/')
    protein=direk+prot+'.pdb'
    input=open(protein,'r')
    strline=input.readline()
    strline=input.readline()
    pt=strline[22:26]
    m=pt.rfind(' ')
    st=int(pt[m:26])
    input.close()
    return(st)
