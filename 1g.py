from collections import Counter
from itertools import izip, tee, islice
s="ACGTTGCATGTCGCATGATGCATGAGAGCT"
f=4
t=tee(s, f)
for i, j in enumerate (t):
	next(islice(j, i, i), None)
p=["".join(k) for k in izip(*t)]
d=Counter(p)
print d