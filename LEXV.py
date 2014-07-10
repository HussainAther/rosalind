import itertools
import collections
o=[]
d=[ ]
q={ }
s=[ ] 
l="EWHNZQAXCI"
w=open("/Users/Mcfoofa/Desktop/rosalindanswers.txt", "a")
h=enumerate(l)
for i in range(5):
	out=[combo for combo in itertools.product(l, repeat=i)]
	d.append(out)
for num, letter in enumerate(l):
	q[num]=letter
for e in d:
	for j in range(len(e)):
		f=""
		u=str(e[j]).strip("(\)\,")
		u=str(e[j]).strip("'")
		if j<4:
			if u<q[j+1]:
				f+=u
		for c in e[j]:
			f+=str(c)
		s.append(f)
for i in range(len(s)):
	if "(" in s[i]:
		a=s[i].find(")")
		s[i]=s[i][a+1:]
		print s[i]
for j in l:
	for i in s:
		if i.startswith(j):
			w.write(i)
			w.write("\n")
# 		if "(" not in i or len(i)==1:
# 			o.append(i)
# 		else:
# 			a=i.find(")")
# 			o.append(i[a+1:])
