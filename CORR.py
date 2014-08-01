#Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:

#s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
#s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).

#Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)

#http://rosalind.info/problems/corr/


f=open("/Users/Mcfoofa/Downloads/rosalind_corr.txt", "r")
l=[]
l1=[]
q=[]
correct=[]
def point_mut_count(original, mutation):
	count = 0
	for i in range(len(original)):
		if mutation[i] != original[i]:
			count +=1
	return count
def complement(text):
	new_text= ""
	for i in text:
		if i == "A":
			new_text+="T"
		elif i == "C":
			new_text+="G"
		elif i == "G":
			new_text+="C"
		else:
			new_text+="A"
	return new_text[::-1]
for i in f.readlines():
    if not i.startswith(">"):
        l.append(str(i.replace("\n", "")))
for i in l:
    if l.count(i)>1:
        correct.append(i)
    elif complement(i) in l:
        correct.append(i)
    else:
        q.append(i)
for i in q:
    c=0
    for j in correct:
        if point_mut_count(i, j)==1:
            if c==0:
                c=1
                l1.append(str(i)+"->"+str(j))
        elif point_mut_count(i, complement(j))==1:
            if c==0:
                c=1
                l1.append(str(i)+"->"+str(complement(j)))
for i in l1:
    print i
