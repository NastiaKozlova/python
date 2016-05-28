import os
part = '/home/nastia/Desktop/HomeoDomain/protein/out/'
partout = '/home/nastia/Desktop/HomeoDomain/protein/end/'
#partoutn = '/home/nastia/Desktop/HomeoDomain/protein/nucleus/'
#outputfile = '/home/nastia/Desktop/vmd_protein.tcl'
list = os.listdir(part)
output = open (outputfile, "w")
#print list
i = 0
for entry in list:
	filename = part + entry 
	os.system('/home/nastia/Desktop/dot2/for_dock/reduce.3.23.130521'+)