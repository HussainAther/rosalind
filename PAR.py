#Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

#Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] for all 1≤i≤q−1, B[q]=A[1], and B[i]>A[1] for all q+1≤i≤n.

#http://rosalind.info/problems/par/

f=open("/Users/Mcfoofa/Downloads/rosalind_par.txt", "r")
c=0
l=[]
for i in f.readlines():
    if c==0:
        c=i.replace("\n", "")
    else:
        l=i.replace("\n", "").split(" ")
#print l
a=l[0]
a1=[]
a2=[]
d=0
e=0
for i in l:
    if d==0:
        d=i
    elif i<a:
        a1.append(i)
    elif i>a:
        a2.append(i)
    elif i==a:
        e+=1
for i in range(e):
    a1.append(a)
a1.append(a)
af=a1+a2
for i in af:
    print i,
