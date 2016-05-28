import Bio.Seq


from Bio.Blast import NCBIWWW

b_parser = NCBIWWW.BlastParser()
b_record = b_parser.parse(b_results)

fasta=open('/home/nastia/fasta_end.txt','r')
string=fasta.readline()
while len(string)>0:
    m=string.find('\t')
    n=string.rfind('\t')
    my_seq_1=Bio.Seq.Seq(string[m+1:n])
    my_seg_2=Bio.Seq.Seq(string[n+1:-1])
    string=fasta.readline()

#dir(Bio.Alphabet)