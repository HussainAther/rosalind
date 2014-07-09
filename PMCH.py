import math
r="UCGGCCUUCCCCUUGUUAGAGCUCGAGCGUCGCAGCGGGAUACCGCUGUACAGGCACAAGUCGUGCGCGUUAAAAGAC"
def pm(x):
	print x
	a=0
	c=0
	for i in x:
		if i =="A":
			a+=1
		if i =="C":
			c+=1
	print math.factorial(a) * math.factorial(c)
pm(r)