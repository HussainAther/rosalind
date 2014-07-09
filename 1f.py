from itertools import tee, izip, islice
s="ACGTTGCATGTCGCATGATGCATGAGAGCT"
t="TATCTCCAC"
c=len(t)
d=tee(s, c)
for i, j in enumerate (d):
	next(islice(j, i, i), None)
p=["".join(k) for k in izip(*d)]
j = [ ]
for i in range(len(p)):
	v=0
	for c in range(len(p[i])):
		if p[i][c]!=t[c]:
			v+=1
	if v<=4:
		j.append(i)
for item in j:
	print item,