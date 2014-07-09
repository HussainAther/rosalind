from urllib2 import urlopen
import itertools
from itertools import tee, izip, islice
import urllib
import fileinput
file=open("/Users/Mcfoofa/Downloads/rosalind_lcsm.txt", "r")
a=[ ]
c=""
for line in file:
	if line.startswith(">")==False:
		c += line.replace("\n", "")
	else:	
		a.append(c)
		c=""
a.append(c)
a.remove("")
p=[ ]
for l in a:
	c=180
	t=tee(l, c)
	for i, j in enumerate (t):
		next(islice(j, i, i), None)
	p.append(["".join(k) for k in izip(*t)])
for q in p[0]:
	t=0
	for y in range(1, len(p)):
		if q in p[y]:
			t+=1
		else:
			t=0
	if t==len(p)-1:
		t=0
		print q 
	else:
		t=0