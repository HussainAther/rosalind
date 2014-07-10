from Bio import Entrez
Entrez.email = "syedather4@yahoo.com"
handle = Entrez.efetch(db="nucleotide", id=["Q55AB5, A2A2Y4"], rettype="fasta")
records = handle.read()
print records
 
