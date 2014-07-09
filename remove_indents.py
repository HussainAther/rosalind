from urllib2 import urlopen
from itertools import tee, izip, islice
import urllib
import fileinput
file=open("/Users/Mcfoofa/Downloads/rosalind-sample.txt", "r")
a=[ ]
c=" "
for line in file:
	if line[0]!=">":
		c = line.replace("\n", "")
		a.append(c)
print a