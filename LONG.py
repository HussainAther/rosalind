import fileinput
import string
file=open("/Users/Mcfoofa/Downloads/rosalind_long-8.txt", "r")
d={ }
c=""
c1=0
for line in file:
	if line.startswith(">")==False:
		c+=line.replace("\n", "")
	else:	
		d[c1]=c
		c=""
		c1+=1
d[c1]=c
del d[0]
for i in d:
	print d[i]
# file.close()
# k=" "
# for j in range(1000, 500, -1):
# 	for i in d:
# 		for x in d:
# 			if d[x][:j]==d[i][-j:] and d[x]!=d[i]:
# 				k=d[i]+d[x][j:]
# 				break
# 		break
# for j in range(1000, 500, -1):
# 	for i in d:
# 		c=k
# 		if d[i][:j]==k[-j:]: 
# 			k+=d[i][j:]
# 		if d[i][-j:]==k[:j]: 
# 			k=d[i][:len(d[i])-j]+c
# print k