from Bio.Align.Applications import MuscleCommandline
muscle_cline = MuscleCommandline('-in /home/nastia/fasta/fasta.fasta -out /home/nastia/fasta/fasta.out -clw -log /home/nastia/fasta/log.txt' )
#muscle_cline = MuscleCommandline( '-in /home/nastia/fasta/fasta.fasta -out /home/nastia/fasta/fasta.phy')
print(muscle_cline)

from Bio import Phylo

tree = Phylo.read("/home/nastia/fasta/fasta.phy", "newick")
tree = tree.as_phyloxml()
Phylo.draw(tree)

#Matplotlib
muscle -maketree -in /home/nastia/fasta/fasta.fasta -out /home/nastia/fasta/fasta.ply -cluster neighborjoining