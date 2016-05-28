direk='/home/nastia/1.10.10.60_1/3g1m/pdb/1.top30/'
import os
lst=os.listdir(direk)
outputfile='3g1m'
output=open('/home/nastia/1.10.10.60_1/3g1m.pml','w')
for entry in lst:
    filename=direk+entry
    outputfilename='/home/nastia/1.10.10.60_1/3g1m'
    output.write('load ' + filename +'\n')
output.write('as cartoon\n' + 'png '+ outputfilename + '.png, width=10cm, dpi=300, ray=1' +'\n')
output.close()