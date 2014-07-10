from __future__ import division
import urllib
import fileinput
file=open("/Users/Mcfoofa/Downloads/rosalind_pdst-3.txt", "r")
a=[ ]
c=""
for line in file:
	if line[0]!=">":
		c += line.replace("\n", "")
	if line.startswith(">"):
		a.append(c)
		c=""
a.append(c)
a.pop(0)
print a
f=[ ] 
for x in a:
	q=""
	for y in a:
		w=0
		for e in range(len(y)):
			if y[e]!=x[e]:
				w+=1
		q+=str(w/len(y))
	f.append(q)
for j in f:
	print j.replace("."," 0.")[2:]
		
