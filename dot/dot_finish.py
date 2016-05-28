fine_n=open('/home/nastia/fine.60.n.txt','r')
strline=fine_n.readline()
list_n=[]

while len(strline)>0:
    list_n.append(strline)
    strline=fine_n.readline()
fine_n.close()
fine_1=open('/home/nastia/fine.60.1.txt','r')
exit=open('/home/nastia/fine.60.txt','w')
exit_not=open('/home/nastia/fine.60_not.txt','w')
strline=fine_1.readline()
while len(strline)>0:
    l=0
    for entry in list_n:
        if strline[0:4]==entry[0:4]:
            exit.write(entry[0:-1]+strline)
            l=l+1
    if l==0:
        exit_not.write(strline)
    strline=fine_1.readline()