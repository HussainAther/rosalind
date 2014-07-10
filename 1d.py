
from itertools import tee, izip, islice
from collections import Counter
s="TCTGACAAACAACGATTGACTGAAGCTACTTTATGTGCGAATTAGT"
c=567
t=[ ]
d=tee(s, c)
for i, j in enumerate (d):
	next(islice(j, i, i), None)
p=["".join(k) for k in izip(*d)]
for z in p:	
	c=12
	d=tee(z, c)
	for i, j in enumerate (d):
		next(islice(j, i, i), None)
	p1=["".join(k) for k in izip(*d)]
	p2=Counter(p1)
	for e in p2:
		if p2[e]>=17:
			t.append(e)
t1=Counter(t)
for y in t1:
	print y,
