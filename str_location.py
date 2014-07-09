s="GATATATATATATAT"
t="ATAT"
n=s.find(t)
print n
n=s.split(t)
k=[ ] 
for item in n:
	if k==[ ]:
		k.append(len(item)+1)
	else:
		k.append(k[-1]+len(t)+len(item))
k.pop()
for item in k:
	print item,