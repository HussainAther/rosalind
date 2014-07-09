import fileinput
s=open("/Users/Mcfoofa/Downloads/rosalind_ini5.txt", "r")
l = [ ] 
for line in s:
	l.append(line)
k=l[1::2]
for item in k:
	print item, 