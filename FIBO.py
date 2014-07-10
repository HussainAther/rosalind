def fib(n): 
	if n==0:
		return 0
	f=[0]*(n+1)
	f[1]=1
	for i in range(2,n+1):
		f[i]=f[i-1]+f[i-2]
	print f
	print f[n]
fib(21)
