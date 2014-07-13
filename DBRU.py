#Given: A collection of up to 1000 DNA strings of equal length (not exceeding 50 bp) corresponding to a set S of (k+1)-mers.

#Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.


f=open("/Users/Mcfoofa/Downloads/rosalind_dbru.txt", "r")
a=[]
a1=[]
a2=[]
a3=[]
a4=[]
b=[]
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
def dbru(a1, a2, b):
    for i in a1:
        for j in a2:
            if i[1:]==j[:-1]:
                if str(i)+", "+str(j) not in b:
                    b.append(str(i)+", "+str(j))
                    print str(i)+", "+str(j)
for i in f.readlines():
    a.append(i.replace("\n", ""))
    a1.append(i.replace("\n", "")[:-1])
    a3.append(complement(i.replace("\n", "")[:-1]))
    a2.append(complement(i.replace("\n", "")[1:]))
dbru(a1, a2, b)
dbru(a2, a1, b)
dbru(a3, a4, b)
dbru(a4, a3, b)
