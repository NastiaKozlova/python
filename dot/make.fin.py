input_file=open('/home/nastia/1.10.10.60_1/3g1m/pdb/1.top30/1.top30.ca.pdb','r')
output=open('/home/nastia/fine.60.1.txt','w')
strline=input_file.readline()
output.write('3g1m\t')
while len(strline)>0:
    
    if strline.find('ATOM')==-1 and strline.find('TER')==-1 and strline.find('REMARK') and strline.find('USER  EDU.SDSC.CCMS.DOT    source file')==-1:
        st=strline[28:-1]
        s=st.find(' ')
        output.write(st[0:s]+'\t')
    strline=input_file.readline()
output.close()
input_file.close()