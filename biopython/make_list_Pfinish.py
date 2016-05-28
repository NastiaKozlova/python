import os
import Bio.SeqIO
#import Bio.SeqIO.FastaIO
#import Bio.AlignIO
#import Bio.Align
#import Bio.Alphabet
#import Bio.Alphabet.IUPAC
#import Bio
import Bio.Seq
from Bio.Alphabet import _verify_alphabet
#help(Bio.SeqIO)
#help(Bio.SeqIO.FastaIO)
#from Bio.Align.Applications import ClustalwCommandline
#help(Bio.Align)
part_name = '/home/nastia/Desktop/fasta/'
list_fasta = os.listdir(part_name)
list_finish = []
for entry in list_fasta:
    data = Bio.SeqIO.FastaIO.SimpleFastaParser(open(part_name+entry))#, (alphabet=Bio.Alphabet.generic_protein))
    for val in data:
        my_seq=Bio.Seq.Seq(val[1], Bio.Alphabet.IUPAC.unambiguous_rna)
        my_seq_1=Bio.Seq.Seq(val[1], Bio.Alphabet.IUPAC.unambiguous_dna)
        my_seq_2=Bio.Seq.Seq(val[1], Bio.Alphabet.IUPAC.protein)
        #print(val)
        #list_finish.append(val)
        if not _verify_alphabet(my_seq) and not _verify_alphabet(my_seq_1) and _verify_alphabet(my_seq_2):
        #if not _verify_alphabet(my_seq):
            list_finish.append(val)
print(len(list_finish))
#for record in list_finish:
    #print(record.alphabet)
    #print(list_finish)
    #cline = ClustalwCommandline('clustalo', infile=list_finish)
#for entry in list_finish:
#cline = MuscleCommandline(input=list_finish, output='/home/nastia/Desktop/fasta.txt')
    #from Bio import AlignIO
    #align = AlignIO.read('/home/nastia/fasta/opuntia.aln', 'clustal')
#/home/nastia/Desktop/fasta