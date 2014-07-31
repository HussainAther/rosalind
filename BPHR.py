#http://rosalind.info/problems/bphr/
#Given: FASTQ file, quality threshold q

#Return: Number of positions where mean base quality falls below given threshold
from __future__ import division
f=open("/Users/Mcfoofa/Downloads/rosalind_bphr_out.txt", "r")
l=[]
for i in f.readlines():
    i=i.replace("\n", "")
    i=i.replace(",", "")
    i=i.replace("[", "")
    i=i.replace("]", "")
    l.append(i.split(" "))
total=len(l)
print total
length=len(l[0])
a=[]*length
for j in range(length):
    avg=0
    for i in l:
        avg+=int(i[j])
    a.append(int(avg)/total)
print a
c=0
for j in a:
    if float(j)<int(27):
        c+=1
print c
