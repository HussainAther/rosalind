from __future__ import division
import math
k=2
n=1
d={ }
f=[ ]
for q in range(k+1):
	d[q]=0
print d
for s in range(k+1):
	f.append(float(math.factorial(k))/float((math.factorial(s)*math.factorial(k-s))))
i=0
print f
for b in f:
	j=k-i
	for c in range(int(b)):
		l=(.75**i)*(.25**j)
		d[i]+=l
	i+=1
print d