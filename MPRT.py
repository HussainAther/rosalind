from urllib2 import urlopen
from itertools import tee, izip, islice
import urllib
import fileinput
file=open("/Users/Mcfoofa/Downloads/rosalind_mprt.txt", "r")
a=[ ]
for line in file:
	line = line.replace("\n", "")
	a.append(line)
print a
v=[ ]
d=" "
for b in a:
	response = urlopen("http://www.uniprot.org/uniprot/" + b + ".fasta").readlines()
	for y in response:
		if y[0]==">":
			v.append(d)
			d=" "
		if y[0]!=">":	
			y=y.replace("\n", "")
			d+=y
v.append(d)
v.remove(" ")
count1=0
print v
for s in v:
	t="NSSN"
	c=4
	t=tee(s, c)
	for i, j in enumerate (t):
		next(islice(j, i, i), None)
	p=["".join(k) for k in izip(*t)]
	#print p
	k=[ ]
	l=[ ]
	z=[ ]
	count=0
	for q in p:
		if q[0]=="N":
			if q[1]!="P":
				if q[2]=="S" or q[2]=="T": 
					if q[3]!="P":
						k.append(q)
						l.append(a[count1]+" "+str(count))
		count+=1
	if l==z:
		l.append(a[count1]+" "+"None")
	count1+=1
#for item in k:
	#print item,
	for f in l:
		print f