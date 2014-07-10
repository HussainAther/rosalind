from __future__ import division
n=916229
d="CTACGACCCA"
y="0.000 0.091 0.162 0.191 0.236 0.346 0.368 0.460 0.504 0.530 0.594 0.685 0.743 0.780 0.830 0.930 1.000"
f=y.split(" ")
e=n-(len(d)-1)
for i in f:
	gc=float(float(i)/2)
	at=float((1-float(i))/2) 
	g=d.count("G")
	a=d.count("A")
	c=d.count("C")
	t=d.count("T")
	print (gc**g)*(gc**c)*(at**a)*(at**t)*e,
