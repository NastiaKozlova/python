def fdna(na, direk):
    import shutil
    #m=na.find('.')
    #dna=na[0:m]
    dst=direk+na+'/'+na+'.cen.allh.pdb'
    src=direk+na+'/'+na+'.cen.polh.xyzq'
    #shutil.copyfile(src, 	dst)
    inputfile=open(dst,'r')
    output=open(src,'w')
    
    xyzg_dna=open('/home/nastia/Desktop/python_ptograms/dot/dna_xyzf.txt','r')
    #/home/nastia/Desktop/python_ptograms/dot/dna_xyzf .txt
    list_dna=[]
    str_dna=xyzg_dna.readline()
    while len(str_dna)>0:
        list_dna.append(str_dna)
        str_dna=xyzg_dna.readline()
    xyzg_dna.close()
    strt =inputfile.readline()
    while len(strt)>0:
        if strt[0:4]=='ATOM':
#            output.write('#'+strt)
            
            for entry in list_dna:
                f=entry.find('\t')
            #if f<2:
                #print(strt[32:55])
                if strt.find(entry[0:f])>0:
                    output.write('#'+strt+'   '+strt[33:56]+entry[f+1:-1])
#                    output.write('   '+strt[32:55]+entry[f+1:-1]+'\n')
        strt=inputfile.readline()
    inputfile.close()
        
    output.close()
    
#    out=direk+dna+'/'+dna+'.cen.polh.xyzq'
#    print(out)
#    print(src)
#    fin=open(out,'w')
#    output=open(src,'r')
#    strline=output.readline()
#    while len(strline)>0:
#        #print(strline)
#        if strline.find('#ATOM')>-1:
#            
#            m= strline.find('@')
#            #print(str(m))
#            #print(strline[0:m]+'\n'+strline[m:-1])
#            n=strline[m:-1].find('@')
#            fin.write(strline[0:m]+'\n'+strline[m+1:-n])
#        strline=output.readline()
    