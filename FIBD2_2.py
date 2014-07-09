n = 6
m = 3
p = {1:1}
k=0
for i in range(n):
	for x in p:
		if p[x]>1 and p[x]<m:
			k+=1
		if p[x]<m and p[x]>0:
			p[x]+=1
		print p
	count=2
	for i in range(k):
		p[count]=1
		count+=1
	k=0
for item in p:
	print p[item]