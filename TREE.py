import fileinput
d={ }
c1=1
file=open("/Users/Mcfoofa/Downloads/rosalind_tree-3.txt", "r")
for line in file:
	line = line.replace("\n", "")
	line = line.replace(" ", ",")
	d[c1]=line
	c1+=1
a=[ ]
def edge_from_a(x):
	e=-1
	for q in x:
		f=x[q].find(",")
		if x[q][0:f] not in a and x[q][f+1:] not in a:
			print x[q][0:f], x[q][f+1:]
			e+=1
		a.append(x[q][0:f])
		a.append(x[q][f+1:])
	print e
edge_from_a(d)
e1=0
for i in range(1, 952):
	if str(i) not in a:
		e1+=1
print e1