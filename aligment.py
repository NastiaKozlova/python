import Bio.Seq
import os 
from Bio.Emboss.Applications import WaterCommandline
from Bio.Align.Applications import ClustalwCommandline

fasta=open('/home/nastia/fasta_end.txt','r')
string=fasta.readline()
outfileput=open('/home/nastia/Desktop/output.txt','w')
while len(string)>0:
    m=string.find('\t')
    n=string.rfind('\t')
    my_seq_1=Bio.Seq.Seq(string[m+1:n])
    my_seg_2=Bio.Seq.Seq(string[n+1:-1])
    cline = WaterCommandline(gapopen=10, gapextend=0.5, asequence=my_seq_1, bsequence=my_seg_2, outfile='/home/nastia/Desktop/Water.txt' )
    #os.system('clustalw'+cline)
    #print(type(cline))
    #print(cline)
    #outfileput.write(cline)
    string=fasta.readline()
outfileput.close()