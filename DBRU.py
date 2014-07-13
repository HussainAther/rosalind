#Given: A collection of up to 1000 DNA strings of equal length (not exceeding 50 bp) corresponding to a set S of (k+1)-mers.

#Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.

f=open("/Users/Mcfoofa/Downloads/rosalind_dbru.txt", "r")
o=open("/Users/Mcfoofa/Downloads/rosalind_dbru_2_output.txt", "a")
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
def dbru(a1, a2, b, a):
    for i in a1:
        for j in a2:
            if i[1:]==j[:-1]:
                if str(i)+str(j[-1]) in a:
                    if str(i)+", "+str(j) not in b:
                        b.append(str(i)+", "+str(j))
                        o.write("("+str(i)+", "+str(j)+")"+"\n")
for i in f.readlines():
    i=i.replace("\n", "")
    a.append(i)
    a.append(complement(i))
    a1.append(i[:-1])
    a2.append(i[1:])
    a3.append((complement(i[:-1])))
    a4.append((complement(i[1:])))
dbru(a4, a3, b, a)
dbru(a1, a2, b, a)
#dbru(a2, a1, b)
#dbru(a3, a4, b)

