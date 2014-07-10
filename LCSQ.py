s="ACACTGTGA"
t="AACCTTGG"
c=[ ]
for j in range(len(t)):
	d=s.find(t[j])
	c.append(s[d])
	s=s[d+1:]
	t=t[j+1:]
	print s
	print t
	print "string"
	for e in c:
		print e,
for y in c:
	print y, 
