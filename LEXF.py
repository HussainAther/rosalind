import itertools
import collections
l="ACGT"
out=[combo for combo in itertools.product(l, repeat=4)]
d={ }
for i in out:
	c= i[0] + i[1] + i[2] + i[3]
	d[c]= 0
print "{"
for i in sorted(d.keys()):
	print "\"" + i + "\"" + ":0," ,
print "}"