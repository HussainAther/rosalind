from __future__ import division
from decimal import *
import math
getcontext().prec=400
n=80
a=[" "]*(n+1)
b=[" "]*(n+1)
for i in range(n+1):
	a[i]=((math.factorial(n)/(math.factorial(n-i)*math.factorial(i))))
	if i<0:
		a[-i]=((math.factorial(n)/(math.factorial(n-i)*math.factorial(i))))
for j in range(1, int(len(a))):
	print 1-float(sum(a[:j])/2**n), 
