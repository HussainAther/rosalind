#http://rosalind.info/problems/cc/

#The task is to use depth-first search to compute the number of connected components in a given undirected graph.

#Given: A simple graph with n≤103 vertices in the edge list format.

#Return: The number of connected components in the graph.



f=open("/Users/Mcfoofa/Downloads/rosalind_cc.txt", "r")
l=[]
l1=[]
l2=[]
c=0
d=0
y = {a : [] for a in range(0,1000)}
for i in f.readlines():
    l.append(i.replace("\n", "").split())
for u in l:
    c=0
    str1=[]
    if u[0] in l1 and u[1] in l1:
        if c==0:
            for j in y:
                if u[0] in y[j] and u[1] not in y[j]:
                    y[j].append(u[1])
                    str1.append(str(j))
                    c=1
                    for j in y:
                        if u[1] in y[j] and u[0] not in y[j]:
                            y[j].append(u[0])
                            str1.append(str(j))
                            str2=str1.sort()
                            if str2 not in l2:
                                l2.append(str2)
                            c=1
                            break
                elif u[1] in y[j] and u[0] not in y[j]:
                    y[j].append(u[0])
                    str1.append(str(j))
                    c=1
                    for j in y:
                        if u[0] in y[j] and u[1] not in y[j]:
                            y[j].append(u[1])
                            str1.append(str(j))
                            str2=str1.sort()
                            if str2 not in l2:
                                l2.append(str2)
                            c=1
                            break
                elif u[1] in y[j] and u[0] in y[j]:
                    break
    elif u[0] not in l1 and u[1] not in l1:
        for z in y:
            if y[z]==[]:
                y[z].append(u[0])
                y[z].append(u[1])
                l1.append(u[0])
                l1.append(u[1])
                break
    else:
        for j in y:
            if u[0] in y[j] and u[1] not in y[j]:
                y[j].append(u[1])
                l1.append(u[1])
                c=1
                break
            elif u[1] in y[j] and u[0] not in y[j]:
                y[j].append(u[0])
                l1.append(u[0])
                c=1
                break
            elif u[1] in y[j] and u[0] in y[j]:
                c=1
                break
l1.sort()
for i in y:
    if y[i]!=[]:
        d+=1
g=len(l2)
print l2
#for i in l2:
#    print i
print l1
for i in range(1, 13):
    if str(i) not in l1:
        d+=1
#print y
print d
print g
print int(d-g)

