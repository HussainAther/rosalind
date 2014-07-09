from __future__ import division
import math
r="GCGGACGCGGACCCGUUUCAACACGCGUUGGUGGUCUUCUAAACUAGUUUACGCAAAUGGGUGGAAAUAAUCCUUGAUGA"
def mm(x):
	a=x.count("A")
	c=x.count("C")
	g=x.count("G")
	u=x.count("U")
	if a>u:
		n1=a
		r1=u
	else:
		r1=a
		n1=u
	if c>g:
		n2=c
		r2=g
	else:
		r2=c
		n2=g
	t1=math.factorial(n1)/math.factorial(n1-r1)
	t2=math.factorial(n2)/math.factorial(n2-r2)
	print int(t1*t2)
mm(r)
