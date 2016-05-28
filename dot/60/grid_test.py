def grid_test(na, prot, direk):
    def xyz_x(strline):
        x_line=strline[27:34]+'n'
        x_n=x_line.rfind(' ')
        if x_n==-1:
            x_s=(x_line[0:-1])
        else:
            x_s=(x_line[x_n:-1])
        x=int(x_s)
        return(x)
    def xyz_y(strline):
        y_s=''
        y_line=strline[38:42]+'n'
        y_n=y_line.rfind(' ')
        if y_n==-1:
            y_s=(y_line[0:-1])
        else:
            y_s=(y_line[y_n:-1])
        y=int(y_s)
        return(y)
    def xyz_z(strline):
        z_s=''
        z_line=strline[46:-5]+'n'
        z_n=z_line.rfind(' ')
        if z_n==-1:
            z_s=(z_line[0:-1])
        else:
            z_s=(z_line[z_n:-1])
        z=int(z_s)
        return(z)
    
#    file_dna=open(direk+na+'.pdb','r')
#    strline=file_dna.readline()
#    strline=file_dna.readline()
#    max_z=xyz_z(strline)
#    min_z=xyz_z(strline)
#    max_y=xyz_y(strline)
#    min_y=xyz_y(strline)
#    max_x=xyz_x(strline)
#    min_x=xyz_x(strline)
#    while len(strline)>4:
#        z=xyz_z(strline)
#        y=xyz_y(strline)
#        x=xyz_x(strline)
#        if z>max_z:
#            max_z=z
#        if y>max_y:
#            max_y=y
#        if x>max_x:
#            max_x=x
#        if z<min_z:
#            min_z=z
#        if y>min_y:
#            min_y=y
#        if x>min_x:
#            min_x=x
#        strline=file_dna.readline()
#    max_x=max_x-min_x
#    max_y=max_y-min_y
#    max_z=max_z-min_z
#    max=max_x
#    if max<max_y:
#        max=max_y
#    if max<max_z:
#        max=max_z
 #   file_dna.close()
 #   print (max)
    file_prot=open(direk+prot+'.pdb','r')    
    strline=file_prot.readline()
    strline=file_prot.readline()
    max_z=xyz_z(strline)
    min_z=xyz_z(strline)
    max_y=xyz_y(strline)
    min_y=xyz_y(strline)
    max_x=xyz_x(strline)
    min_x=xyz_x(strline)
    while len(strline)>4:
        print(strline)
        z=xyz_z(strline)
        y=xyz_y(strline)
        x=xyz_x(strline)
        if z>max_z:
            max_z=z
        if y>max_y:
            max_y=y
        if x>max_x:
            max_x=x
        if z<min_z:
            min_z=z
        if y>min_y:
            min_y=y
        if x>min_x:
            min_x=x
        strline=file_prot.readline()
    max_x=max_x-min_x
    max_y=max_y-min_y
    max_z=max_z-min_z
    max=max_x
    if max<max_y:
        max=max_y
    if max<max_z:
        max=max_z
    print(max)
    file_prot.close()
    return(max)