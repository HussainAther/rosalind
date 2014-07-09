n=6
m=3
p=[1]
k=[ ]
for i in range(n):
	for x in range(len(p)):
		if p[x]==1:
			p[x]+=1
		else:
			p[x]+=1
			k.append(1)
			if p[x]==m:
				p[x]==0
	for j in k:
		p.append(j)
	del k[:]
	print p