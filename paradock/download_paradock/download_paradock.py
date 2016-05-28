#import wget
import urllib2, os
from donload_from_internet import *
from zip_ecs import *
outpart = '/home/nastia/Desktop/protein/'
inputfile = '/home/nastia/Desktop/paradock.txt'
outputfile = '/home/nastia/Desktop/protein.txt'

output_file = open(outputfile, 'w')
input_file = open (inputfile, 'r')
st = input_file.readline()
while len(st) > 0:
    url = st
    name = url[44:48]
    st = input_file.readline()
    part = outpart + name +'/'
    st = input_file.readline()
    output_file.write (name+ '\n')
    file_name = part + 'paradock.zip'

    print(file_name +' ' + url)

    download_from_internet(url, file_name)
    unzip (file_name,part)
output_file.close() 
input_file.close()

print ('done')