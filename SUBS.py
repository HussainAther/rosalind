from itertools import tee, izip, islice
s="ACCGTGAACCGTGAGGA"
t="ACCGTGAAC"
c=len(t)
d=tee(s, c)
for i, j in enumerate (d):
	next(islice(j, i, i), None)
p=["".join(k) for k in izip(*d)]
j = [ ]
count = 0
print p
for i in p:
	if i==t:
		j.append(count)
	count+=1
for item in j:
	print item,
		 
