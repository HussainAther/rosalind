import fileinput
import string
s=open("/Users/Mcfoofa/Downloads/rosalind_grph-4.txt", "r")
l = [ ]
for line in s:
	line=line.replace("\n", "")
	l.append(line)
#print l
p = { }
count = 0
for item in l:
	if item[0]==">":
		w=item[1:]
		p[w]=l[count+1]+l[count+2]
		count+=1
	else:
		count+=1
print p
# k = [ ] 
# s.close()
# for i in p:
# 	c=p[i][-3::]
# 	o=i
# 	for x in p:
# 		if p[x][:3:]==c and x!=o:
# 			k.append(x)
# 			k.append(o)
# l1=[ ]
# l2=[ ]
# j=0
# for val in k:
# 	if j%2!=0:
# 		l1.append(val)
# 		j+=1
# 	else:
# 		l2.append(val)
# 		j+=1
# for key, value in zip(l1, l2):
# 	print key, value