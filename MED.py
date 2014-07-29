#Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

#Return: A sorted array A[1..n].

#http://rosalind.info/problems/med/


f=open("/Users/Mcfoofa/Downloads/rosalind_med-2.txt", "r")
c=0
k=0
l=[]
for i in f.readlines():
    if c==1:
        a=i.replace("\n", "").split(" ")
        for j in a:
            l.append(int(j))
    elif c==2:
        k=i.replace("\n", "")
    c+=1
print l
print k
a=sorted(l)
print a[int(k)-1]
