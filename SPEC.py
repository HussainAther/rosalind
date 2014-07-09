f=open("/Users/Mcfoofa/Downloads/rosalind_spec.txt", "r")
l=[]
e=""
#d={'A': 71.03711,
#    'C': 103.00919,
#    'D': 115.02694,
#    'E': 129.04259,
#    'F': 147.06841,
#    'G': 57.02146,
#    'H': 137.05891,
#    'I': 113.08406,
#    'K': 128.09496,
#    'L': 113.08406,
#    'M': 131.04049,
#    'N': 114.04293,
#    'P': 97.05276,
#    'Q': 128.05858,
#    'R': 156.10111,
#    'S': 87.03203,
#    'T': 101.04768,
#    'V': 99.06841,
#    'W': 186.07931,
#    'Y': 163.06333}
d={'A': 71,
    'C': 103,
    'D': 115,
    'E': 129,
    'F': 147,
    'G': 57,
    'H': 137,
    'I': 113,
    'K': 128.09,
    'L': 113,
    'M': 131,
    'N': 114,
    'P': 97,
    'Q': 128.06,
    'R': 156,
    'S': 87,
    'T': 101,
    'V': 99,
    'W': 186,
    'Y': 163}
l1=[]
s=0
for i in f.readlines():
    l.append(i.replace("\n", ""))
for i in l:
    if s>1:
        if int(round((float(i)-float(s)),0))==128:
            if round((float(i)-float(s)),2)==128.06:
                l1.append(128.06)
            elif round((float(i)-float(s)),2)==128.10 or round((float(i)-float(s)),2)==128.09:
                l1.append(128.09)
        else:
            l1.append(int((round(float(i)-float(s),0))))
    s=float(i)
print l1
for i in l1:
    for j in d:
        if d[j]==i:
            e+=j
            break
print e