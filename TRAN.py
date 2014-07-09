from __future__ import division
import fileinput
import string
def tran_count(original, mutation):
	transition_count = 0
	transversion_count = 0
	for i in range(len(original)):
		if mutation[i] != original[i]:
			if mutation[i]=="C" and original[i]=="T":
				transition_count +=1
			elif mutation[i]=="T" and original[i]=="C":
				transition_count +=1
			elif mutation[i]=="G" and original[i]=="A":
				transition_count +=1
			elif mutation[i]=="A" and original[i]=="G":
				transition_count +=1
			else:
				transversion_count+=1
	ratio = float(transition_count/transversion_count)
	print ratio
file=open("/Users/Mcfoofa/Downloads/sample_tran.txt", "r")
d={ }
c=""
c1=0
for line in file:
	if line.startswith(">")==False:
		c+=line.replace("\n", "")
	else:	
		d[c1]=c
		c=""
		c1+=1
d[c1]=c
del d[0]
tran_count(d[1], d[2])
