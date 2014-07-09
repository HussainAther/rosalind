f=open("/Users/Mcfoofa/Downloads/rosalind-deg.txt", "r")
n=1000
l={}
for i in range(1,n+1):
	l[i]=0
print l
for i in f.readlines():
	l[int(i.split(" ")[0].replace("\n", ""))]+=1
	l[int(i.split(" ")[1].replace("\n", ""))]+=1
for i in l:
	print l[i],