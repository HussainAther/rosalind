#Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

#Return: A sorted array A[1..n].

#http://rosalind.info/problems/qs/

f=open("/Users/Mcfoofa/Downloads/rosalind_qs-2.txt", "r")
c=0
k=0
l=[]
a=[]
b=[]
for i in f.readlines():
    if c==1:
        a=i.replace("\n", "").split(" ")
        for j in a:
            l.append(int(j))
    c+=1
l1=sorted(l)
#for i in l1:
#    print i,
def part(l):
    a=[]
    b=[]
    c=[]
    if len(l)>1:
        x=l[0]
        for i in l[1:]:
            if int(i)<int(x):
                a.append(i)
            elif int(i)>int(x):
                b.append(i)
            elif int(i)==int(x):
                c.append(i)
        c.append(x)
        a=part(a)
        b=part(b)
        d=a+c+b
        return d
    else:
        return l
d=part(l)
for i in d:
    print i,
