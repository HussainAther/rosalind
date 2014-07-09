T="GATATATGCATATACTT"
p="ATAT"
m=4
n=len(T)
for i in range(n - m):
    has_match=True
    for j in range(m):
        if p[j] != T[i+j]: 
            has_match==False
            break
    if has_match=True:
    	print j