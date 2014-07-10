import fileinput
import math
f=open("/Users/Mcfoofa/Downloads/rosalind_nwck-2.txt")
for line in f:
	print line
	if line[0].isalpha():
		e=line.split(" ")[0]
		g=line.split(" ")[1]
		a=2
		b=abs(prevLine.find(e))
		h=abs(prevLine.find(g)) 
		if b<h:
			for z in prevLine[b:h]:
				if z=="(":	
					a+=1
				if z==")":
					a-=1
		else:
			for z in prevLine[h:b]:
				if z=="(":	
					a+=1
				if z==")":
					a-=1
		print a,
	prevLine=line
