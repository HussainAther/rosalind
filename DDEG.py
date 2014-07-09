f=open("/Users/Mcfoofa/Downloads/rosalind_ddeg.txt", "r")
n=1000
l={}
c=[ ]
for i in range(1,n+1):
	l[i]=""
for i in f.readlines():
	l[int(i.split(" ")[0].replace("\n", ""))]+=str(i.split(" ")[1].replace("\n", "") + " ")
	l[int(i.split(" ")[1].replace("\n", ""))]+=str(i.split(" ")[0].replace("\n", "") + " ")
print l
for i in l:
	d=0
	for j in l[i].split(" "):
		if j.isdigit():
			d+=int(len(str(l[int(j)][:-1]).split(" ")))
	c.append(d)
for i in c:
	print i,