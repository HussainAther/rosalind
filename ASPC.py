import math 
n=1689
m=679
def nCr(t,r):
	f=math.factorial
	return f(t)/f(r)/f(t-r)
e=0
for i in range(m, n+1):
	e+=nCr(n, i)
print e % 1000000
