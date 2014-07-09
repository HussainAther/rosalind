import re
s="TAGCGGATAAGGAACACGAGAA"
n=""
c=""
for j in s:
	if j=="A":
		n+="T"
	if j=="C":
		n+="G"
	if j=="T":
		n+="A"
	if j=="G":
		n+="C"
for i in range(1, len(n)+1):
	c+=n[-i]
print c.replace(" ","")