input=open('/home/nastia/fine.60.txt','r')
import os
part_prot = '/home/nastia/Desktop/dot_60/1.10.10.60/'
strline=input.readline()
while len(strline)>0:
    prot=strline[0:4]
    
    direc=part_prot+prot+'/'+prot+'_n/latest/pdb/' 

    output=open('/home/nastia/pymol_n/'+prot+'.pml','w')
    if os.path.exists(direc):
        list1 = os.listdir(direc)

        for entry in list1:
            #UNP
            dit=direc+entry+'/'
            list3 = os.listdir(dit)
            for nom in list3:
                if entry.find('.top30.ca.pdb')==-1:
                    output.write('load '+dit+nom+'\n')
        output.write('as cartoon\npng /home/nastia/Practice_1/'+prot+'.png, width=10cm, dpi=300, ray=1\n')
    output.close()
    ditec=part_prot+prot+'/'+prot+'_1/latest/pdb/'
    output=open('/home/nastia/pymol_1/'+prot+'.pml','w')
    if os.path.exists(ditec):
        list2 = os.listdir(ditec)
        #print (list2)
        for entry in list2:
            dit=ditec+entry+'/'
            list4 = os.listdir(dit)
            for nom in list4:
                if nom.find('.top30.ca.pdb')==-1:
                    output.write('load '+dit+nom+'\n')
        output.write('as cartoon\npng /home/nastia/Practice_n/'+prot+'.png, width=10cm, dpi=300, ray=1\n')
    output.close()

    strline=input.readline()

