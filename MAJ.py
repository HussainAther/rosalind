f=open("/Users/Mcfoofa/Downloads/rosalind-maj.txt", "r")
c=[]
q=[]
g=[]
d=0
e=0
l=0
for i in f.read().split(" "):
	l+=1
	g.append(i.replace("\n", ""))
	if l==8094:
		l=0
		q.append(g)
		print "YEA"
		g=[]
q.append(g)
# print q
for i in q:
	for j in i:
		if e==0:
			e=i.count(j)
			d=j 
		elif i.count(j)>e:
			e=i.count(j)
			d=j
	if e>8094/2:
		c.append(d)
	else:
		c.append(-1)
	e=0
	d=0
for y in c:
	print y,
