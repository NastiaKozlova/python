#load /home/nastia/Nastia/Practice1/4YRV.pdb
#as cartoon
#png /home/nastia/Nastia/Practice1/cartoon.png, width=10cm, dpi=300, ray=1

import os
part = '/home/nastia/Desktop/protein/1bjz/paradock/'
#partout = '/home/nastia/Desktop/HomeoDomain/protein/pymol/'
outputfile = '/home/nastia/Desktop/pymol.pml'
list = os.listdir(part)
output = open (outputfile, "w")
#print list
i = 0
for entry in list:
    filename = part + entry 
    #name = entery[0:4]
#   outputfilename = partout + entry
    output.write('load ' + filename +'\n')
#   output.write('load ' + filename + '\n' + 'as cartoon\n' + 'png '+ outputfilename + '.png, width=10cm, dpi=300, ray=1' +'\n' +'as lines\n')
output.write('as cartoon\n' + 'png '+ outputfilename + '.png, width=10cm, dpi=300, ray=1' +'\n' +'as lines\n')
output.close()
print ('done')