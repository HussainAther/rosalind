import operator
f=open("/Users/Mcfoofa/Downloads/rosalind_prsm.txt", "r")
d={'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333}
k=0
c=0
g=10
s=[]
n=[]
m=[]
u={}
u1={}
for i in f.readlines():
    if k==0:
        g=int(i.replace("\n", ""))+1
    elif k<g and k>0:
        s.append(i.replace("\n", ""))
    elif k>=g:
        n.append(i.replace("\n", ""))
    k+=1
for i in s:
    l=[]
    for j in i:
        l.append(d[j])
    m.append(l)
for i in m:
    c+=1
    for j in i:
        for e in n:
            if str(c)+ " " +str(round((float(e)-float(j)),5)) not in u:
                u[str(c)+ " " +str(round((float(e)-float(j)),5))]=1
            else:
                u[str(c)+ " "+str(round((float(e)-float(j)),5))]+=1
            if str(round((float(e)-float(j)),5)) not in u1:
                u1[str(round((float(e)-float(j)),5))]=1
            else:
                u1[str(round((float(e)-float(j)),5))]+=1
print sorted(u.iteritems(), key=operator.itemgetter(1))[-1]
print sorted(u1.iteritems(), key=operator.itemgetter(1))[-1]
#y=sorted(u1.iteritems(), key=operator.itemgetter(1))[-1][0]
#for i in u:
#    if str(i.split()[1])==str(y):
#       print i