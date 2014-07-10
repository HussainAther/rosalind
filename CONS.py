import fileinput
d_a={ }
d_c={ }
d_g={ }
d_t={ }
f=open("/Users/Mcfoofa/Downloads/rosalind_cons-2.txt", "r+")
j={ }
count2=0
str=""
for line in f.readlines():
	if line.startswith("A") or line.startswith("C") or line.startswith("G") or line.startswith("T"):
		str+=line 
		str=str.replace("\n", "")
	if line.startswith(">"):
		j[count2]=str
		str=""
		count2+=1
f.close()
j[count2]=str
j.pop(0)
count=0
for q in j:
	for c in range(len(j[q])):
		d_a[c]=0
		d_g[c]=0
		d_t[c]=0
		d_c[c]=0
	break
for l in j:
	count=0
	for z in j[l]:
		if z=="A":
			d_a[count]+=1
		if z=="C": 
			d_c[count]+=1
		if z=="G":
			d_g[count]+=1
		if z=="T":
			d_t[count]+=1
		count+=1
o={ }
for i in d_a:
	o[i]="A"
for i in d_c:
	if d_c[i]>d_a[i]:
		o[i]="C"
for i in d_g:
	if d_g[i]>d_a[i] and d_g[i]>d_c[i]:
		o[i]="G"
for i in d_t:
	if d_t[i]>d_a[i] and d_t[i]>d_c[i] and d_t[i]>d_g[i]:
		o[i]="T"
str=""
for i in o:
	str+=o[i]
print str
print "\n"
for i in d_a:
	print d_a[i],
print "\n"
for i in d_g:
	print d_c[i],
print "\n"
for i in d_c:
	print d_g[i],
print "\n"
for i in d_t:
	print d_t[i],
