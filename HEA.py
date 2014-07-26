#http://rosalind.info/problems/hea/

#Given: A positive integer n≤105 and array A[1..n] of integers from −105 to 105.

#Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].

f=open("/Users/Mcfoofa/Downloads/rosalind_hea-8.txt", "r")
c=0
l=[]
n=""
l = {a : "" for a in range(0,100000)}
for i in f.readlines():
    if c==0:
        n=i.replace("\n", "")
        c+=1
    else:
        for j in i.split(" "):
            l[c]=int(j.replace("\n", ""))
            c+=1
#for i in l:
#    print i,
dele=[]
for i in l:
    if l[i]=="":
        dele.append(i)
for i in dele:
    del l[i]
n=len(l)
print n
#print l
print "\n"
for i in range(1, len(l)):
    if l[i]==max(l):
        a=l[1]
        l[1]=l[i]
        l[i]=a
        break
def check(l, i):
    if l[i/2]<l[i]:
        a=l[i]
        l[i]=l[i/2]
        l[i/2]=a
    return l
def overall_check(l):
    for i in range(2, n+1):
        l=check(l, i)
    for i in range(2, n+1):
        if l[i/2]<l[i]:
            overall_check(l)
overall_check(l)
for i in l:
    print l[i],
