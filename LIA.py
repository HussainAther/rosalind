from __future__ import division
import math
k=6
n=15
t=2**k
i=0
s=[ ] #the prob of each individual being heterozygous
p=[ ] #the prob of a certain number of individuals being heterozygous
for q in range(t+1):
	j=t-i
	print j, i
	f=(float(math.factorial(t))/float((math.factorial(j)*math.factorial(t-j))))
	s.append((.25**i)*(.75**j)*f)
	i+=1
print s
print sum(s[n:])