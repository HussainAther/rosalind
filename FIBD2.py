n=6
m=3
p=[1]
y=[ ]
k=[ ]
for i in range(n):
	for x in range(len(p)):
		if p[x]<=m and p[x]>0:
			p[x]+=1
			if p[x]>1:
				y.append(1)
		else:
			p[x]=0
	print p
	for j in y:
		p.append(j)