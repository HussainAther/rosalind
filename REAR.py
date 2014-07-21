#http://rosalind.info/problems/rear/

#A reversal of a permutation creates a new permutation by inverting some interval of the permutation; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5) are all reversals of (5,3,2,1,4). The reversal distance between two permutations π and σ, written drev(π,σ), is the minimum number of reversals required to transform π into σ (this assumes that π and σ have the same length).

#Given: A collection of at most 5 pairs of permutations, all of which have length 10.

#Return: The reversal distance between each permutation pair.


import distance
import operator
import sys
f=open("/Users/Mcfoofa/Downloads/rosalind_rear.txt", "r")
o=open("/Users/Mcfoofa/Downloads/rosalind_rear_test.txt", "a")
a=[]
b=[]
c=[]
list=[]
d=0 #distance of most misplaced number
e=0 #number that is most displaced
reverses=0
count1=[]
min_dist=10
for i in range(12):
    count1.append(i)
#def listfind(list, value):
#    for j in range(len(list)):
#        if list[j]==value:
#            return j
#def singleham(x, y, z, u): #finds distance of most misplaced number
#    z1=listfind(x, z)
#    z2=listfind(y, z)
#    if abs(z1-z2) > u:
#        u=abs(z1-z2)
#    return z
#def invert(b, c, d, reverses):
#    for i in b:
#        e=singleham(b, c, q, d)
#    b1=b[:listfind(b, e)+1]
#    b2=b[listfind(b, e)+1:]
#    b1.reverse()
#    reverses+=1
#    b=b1+b2
#    if b!=c:
#        d=0
#        invert(b, c, d, reverses)
#    else:
#        print reverses
#for i in f.readlines():
#    a.append(i.replace("\n", "").split(" "))
#for i in a:
#    if i==['']:
#        reverses=0
#        invert(b, c, d, reverses)
#        d=0
#        b=[]
#        c=[]
#    if b==[]:
#        b=i
#    elif b and c==[]:
#        c=i
def search(a, b, count, min_dist):
    min_list=[]
    l={}
    if distance.hamming(a, b)==0:
        print count
        print a
        sys.exit()
        return
    count+=1
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if i==0 and j==0:
                a1=a[j:i+1:-1]+a[j:]
            elif i==0 and j>0:
                a1=a[j::-1]+a[i+j+1:]
            else:
                a1=a[:i]+a[j+1:i-1:-1]+a[j+2:]
            str1=""
            for q in a1:
                str1+=q
                str1+=" "
            #print str(j)+str(a1)
            l[str1]=distance.hamming(a1, b)
#            if distance.hamming(a1, b)<min_dist:
#                l[a1]=distance.hamming(a1, b)
#            if distance.hamming(a1, b)==0:
#                print count
#                print a1
#                sys.exit()
#                return

    l1=sorted(l.iteritems(), key=operator.itemgetter(1))
    for i in l1:
        if i[1]==l1[0][1] and i[1]<min_dist:
            min_list.append(i[0].split())
    for i in l1:
        if i[1]==l1[0][1]:
            min_dist=i[1]
    for i in min_list:
        o.write(str(i)+"\t"+str(count)+"\n")
        my_count=count
        my_dist=min_dist
        search(i, b, my_count, my_dist)
    return
for i in f.readlines():
    i=i.replace("\n", "").split(" ")
    if len(i)>2:
        a.append(i)
for i in a:
    if b==[]:
        b=i
    elif b and c==[]:
        c=i
    else:
        count=0
        search(b, c, count, min_dist)
        sys.exit()
        count=0
        min_dist=10
        b=[]
        c=[]


####### WRITE AN ALGORITMH THAT COUNTS THE NUMBER OF BREAKPOOINTS INSTEAD OF USING THE HAMMING DITSTANCE, DUDE!############

