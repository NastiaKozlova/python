output_file='/home/nastia/output_fasta_global.txt'
in_file='/home/nastia/fasta_end.txt'
import Bio
import Bio.Seq
import Bio.Alphabet
import Bio.pairwise2
output_fasta = open(output_file, 'w')
fasta = open(in_file, 'r')
strline = fasta.readline()
seq_2=''
while len(strline)>0:
    m = strline.find('\t')
    n=strline.rfind('\t')
    my_seq_1=strline[m+1:n]
    my_seq_2=strline[n+1:-1]
    seq_1=Bio.Seq.Seq(my_seq_1, Bio.Alphabet.IUPAC.unambiguous_dna)
    seq_2=Bio.Seq.Seq(my_seq_2, Bio.Alphabet.IUPAC.unambiguous_dna)
    output_fasta.write('> '+strline[0:m]+ '\n')
    print(strline[0:m])
    #for a in Bio.pairwise2.align.localxx(seq_1, seq_2):
    for a in Bio.pairwise2.align.globalxx(seq_1, seq_2):
        output_fasta.write(Bio.pairwise2.format_alignment(*a))
    strline=fasta.readline()
output_fasta.write('> test\n')
output_fasta.close()
fasta.close()
finish_file=open('/home/nastia/nastia.txt','w')
test=open(output_file,'r')
strline=test.readline()
m=0
while not len(strline)==0:
    if strline.find('>')==0:
        finish_file.write('\n'+strline[0:-1]+'\t')
        m=0
    else:
        if strline.find('Score')>-1:
            if m==0:
                finish_file.write(strline[8:-1]+'\t')
                m=m+1
    strline=test.readline()
test.close()
