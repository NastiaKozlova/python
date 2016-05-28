from Bio.Align.Applications import ClustalwCommandline
import os
cline = ClustalwCommandline('clustalo', infile='/home/nastia/fasta/opuntia.fasta')
#os.system('clustalw'+ 'infile="/home/nastia/fasta.fasta"'+'outfile)
print(cline)
from Bio import AlignIO
align = AlignIO.read('/home/nastia/fasta/opuntia.aln', 'clustal')
print(align)