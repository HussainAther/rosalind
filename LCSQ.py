#Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
#Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)


from numpy import zeros
f=open('/Users/Mcfoofa/Downloads/rosalind_lcsq-2.txt', 'r')
c1=""
c2=""
c=0
for i in f.readlines():
    if i.startswith(">") and c1!="":
        c+=1
    elif not i.startswith(">") and c==0:
        c1+=i.replace("\n", "")
    elif not i.startswith(">") and c==1:
        c2+=i.replace("\n", "")
c = zeros((len(a)+1,len(b)+1))
def func2(i, j):
  while i!=0 and j!=0:
    if i == 0 or j == 0:
        return ""
    elif a[i-1] == a[j-1]:
        return func2(i-1, j-1) + [a[i-1]]
    elif c[i-1, j] > c[i, j-1]: 
        return func2(i-1, j)
    else:
        return func2(i, j-1)
    return l
def func(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c[i+1][j+1] = c[i][j]+1
            else:
                c[i+1][j+1] = max(c[i+1][j],c[i][j+1])
    l=""
    i,j = len(a), len(b)
    l=func2(i, j)
    return l
q = func(c1,c2)
print q
