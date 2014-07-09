from __future__ import division
import urllib
import fileinput
file=open("/Users/Mcfoofa/Downloads/rosalind_meme.txt", "r")
a=[ ]
c=""
for line in file:
	if line[0]!=">":
		c += line.replace("\n", "")
	if line.startswith(">"):
		a.append(c)
		c=""
a.append(c)
a.pop(0)
for i in a:
	print i