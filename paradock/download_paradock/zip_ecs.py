def unzip (file_name,part):
    import zipfile
    z=zipfile.ZipFile(file_name,"r")
    zl=z.namelist()
    partt=part+'paradock/'
    print('+' + partt)
    z.extractall(partt)
    z.close()