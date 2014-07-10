from itertools import permutations
n=2
a=[ ]
b=[ ]
def array(n):
	a=[ ]
	for i in range(1,n+1):
		a.append(i)
		a.append(-i)
	return perm(a, n)

def perm(a, n):
	c=0
	for y in permutations(a, n):
		works(y)
	
def works(y):
	b=[ ]
	v=0 
	for q in range(1, n+1):
		if y.count(q)==1 or y.count(-q)==1:
			v+=1
		if v==n:
			b.append(y)
	for i in b:
		for c in i:
			print c,
		print "\t"
