from urllib2 import urlopen
from itertools import tee, izip, islice
import urllib
import fileinput
file=open("/Users/Mcfoofa/Downloads/sample.txt", "r")
a=[ ]
c=" "
for line in file:
	if line.startswith(">")==False:
		c += line.replace("\n", "")
	else:	
		a.append(c)
		c=" "
a.append(c)
a.remove(" ")
print a