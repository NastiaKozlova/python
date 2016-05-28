input=open('C:/Users/Sergey/Desktop/dna_sec/test20.txt','r')
out=open('C:/Users/Sergey/Desktop/dna.txt','w')
strline=input.readline()
while strline>0:
	out.write(strline[0:20]+'\n')
	strline=input.readline()
input.close()
out.close()