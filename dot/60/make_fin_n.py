def make_fin(ditec,prot,na):
    input_file=open(ditec+'latest/'+'pdb/'+na+'.top30/'+na+'.top30.ca.pdb','r')
    output=open('/home/nastia/fine.60.n.txt','a')
    strline=input_file.readline()
    output.write(prot+'\t')
    while len(strline)>0:
    
        if strline.find('ATOM')==-1 and strline.find('TER')==-1 and strline.find('REMARK') and strline.find('USER  EDU.SDSC.CCMS.DOT    source file')==-1:
            st=strline[28:-1]
            s=st[1:-1].find(' ')
            output.write(st[0:s]+'\t')
        strline=input_file.readline()
    output.write('\n')
    output.close()
    input_file.close()