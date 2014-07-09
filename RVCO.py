from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
f=open("/Users/Mcfoofa/Downloads/rosalind_rvco-3.txt", "r")
count=0
for i in f.readlines():
	if not i.startswith(">"):
		my_seq = Seq(i, IUPAC.unambiguous_dna)
		a=str(my_seq.strip()).replace(" ","")
		b=str(my_seq.reverse_complement().strip()).replace(" ","")
		if a==b:
			count+=1
print count