def recurrance(m, k):
	o=1
	y=0 
	for i in range(3, m+1):
			no=y
			ny=k*o
			o+=no
			y=ny	 
	return o+y
