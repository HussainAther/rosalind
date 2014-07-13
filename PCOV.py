Given: A collection of (error-free) DNA k-mers (k≤50) taken from the same strand of a circular chromosome. In this dataset, all k-mers from this strand of the chromosome are present, and their de Bruijn graph consists of exactly one simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic chromosome).


f=open("/Users/Mcfoofa/Downloads/rosalind_pcov.txt", "r")
a=[]
b=""
def singlepcov(i, b):
    for q in range(len(i),0, -1):
        if i[:q]==b[-q:]:
            print "strings " + str(i)+" "+str(b)
            b=str(i[:q])+str(b[-q:])
            return b
        elif b[:q]==i[-q:]:
            print "strings " + str(i)+" "+str(b)
            b=str(b[:q])+str(i[-q:])
            return b
    return b
def pcov(i, j, b):
    if i[1:]==j[:-1]:
        b=str(i)+str(j[-1])
    return b
for i in f.readlines():
    i=i.replace("\n", "")
    a.append(i)
print a
for i in a:
    for j in a:
        if b=="":
            b=pcov(i, j, b)
print b
for i in a:
    b=singlepcov(i, b)
#print b
