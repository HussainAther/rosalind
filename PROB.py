from __future__ import division
import math
s="CCCCGGTCTGTCAGAAACGAGTCCCGGTCGTCCGTGCTAGGTTCATAGGAATTGCAGTCTTTAGCCACGTTGTAGGACCCTGCT"
d="0.057 0.154 0.168 0.233 0.277 0.351 0.412 0.422 0.487 0.568 0.625 0.632 0.705 0.738 0.830 0.865 0.938"
e=d.split(" ")
print e
a=s.count("A")+s.count("T")
c=s.count("C")+s.count("G")
for i in e:
	gc=float(float(i)/2)
	at=float((1-float(i))/2)
	t=(gc**c)*(at**a)
	print math.log10(t),