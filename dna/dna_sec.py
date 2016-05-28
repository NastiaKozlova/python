out1=open('C:/Users/Sergey/Desktop/dna_sec/1.txt','w')
out1.write('a\nc\ng\nt\n')
out1.close()

def rrr(entry):
#	test=open('C:/Users/Sergey/Desktop/strnot.txt','w')
	strnot=''
	for lenstr in range(len(entry)):
		#print(lenstr)
		if entry[lenstr]=='t':
			bp='a'
		elif entry[lenstr]=='a':
			bp='t'
		elif entry[lenstr]=='c':
			bp='g'
		elif entry[lenstr]=='g':
			bp='c'
		strnot=strnot+bp
		
#		test.write(strnot)
#	test.close()
	return strnot
	#print(strnot)
def ttt(entry):
#	test=open('C:/Users/Sergey/Desktop/strnot.txt','w')
	n=len(entry)
	retorn=''
	for lenstr in range (n):
		retorn=retorn+entry[n-lenstr-1]
	return retorn

def nnn(entry):
#	test=open('C:/Users/Sergey/Desktop/strnot.txt','w')
	n=len(entry)
	strnot=rrr(entry)
	retorn=''
	for lenstr in range (n):
		retorn=retorn+strnot[n-lenstr-1]
	return retorn

for m in range(19):
	file_m1='C:/Users/Sergey/Desktop/dna_sec/'+str(m+1)+'.txt'
	file_m2='C:/Users/Sergey/Desktop/dna_sec/'+str(m+2)+'.txt'
	#print(file_m1+'  '+file_m2)
	outin=open(file_m1,'r')
	listy=[]
	strline=outin.readline()
	
	lensec=len(strline)
	while lensec>0:
		listy.append(strline[0:-1])
		strline=outin.readline()
		lensec=len(strline)
	s=set()
	#n=0
	for entry in listy:
		#print('###   '+entry)
		if not (s.__contains__(entry) or s.__contains__(rrr(entry))or s.__contains__(ttt(entry)) or s.__contains__(nnn(entry))):
			s.add(entry) 
			#print('&&&   '+entry)
			#n=n+1
			#print(str(n))
	#print(s)
	#print('number of elements '+str(n))
	#print('file writing '+str(m+2))
	outin.close()

#	outin=open('C:/Users/Sergey/Desktop/dna_sec/'+str(m+1)+'.txt','r')
	out=open(file_m2,'w')
	for elem in s:
		len_elem=len(elem)
		#print('len_elem '+ str(len_elem))
		if len_elem>1:
			if not elem[len_elem-2:len_elem]=='aa':
				out.write(elem+'a\n')
				#print('1 '+elem[len_elem-3:len_elem])
				#print('2 '+elem)
			if not elem[len_elem-2:len_elem]=='tt':
#				print(elem[-1])
				out.write(elem+'t\n')
			if not elem[len_elem-2:len_elem]=='gg':
#				print(elem[-3:-1])
				out.write(elem+'g\n')
			if not elem[len_elem-2:len_elem]=='cc':
#				print(elem[-3:-1])
				out.write(elem+'c\n')
		else:
			out.write(elem+'a\n')
			out.write(elem+'t\n')
			out.write(elem+'g\n')
			out.write(elem+'c\n')
	out.close()

	print(str(m+2))
#	out.close()
#	outin.close()
	
#	input=open('C:/Users/Sergey/Desktop/dna_sec/'+str(m+2)+'.txt','r')
#	output=open('C:/Users/Sergey/Desktop/dna_sec/'+str(m+2)+'.txt','w')
#	str1 = input.readline()
#	list = []
#	while len(str1)>0:
#		list.append(str1)
#		str1 = input.readline()
#	list.sort()
#	lastsdr = ''
#	for entry in list:
#		if lastsdr == entry: 
#			lastsdr = entry
#		else:
#			output.write(entry)
#			lastsdr = entry
#		
#	list = []
#	while len(str1)>0:
#		list.append(str1)
#		str1 = input.readline()
#	list.sort()
#	lastsdr = ''
#	for entry in list:
#		output.write(entry)
#		
#		entryover=
#	input.close()
#	output.close()