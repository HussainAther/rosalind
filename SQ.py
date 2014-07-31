#Given: A positive integer k≤20 and k simple undirected graphs with n≤400 vertices in the edge list format.

#Return: For each graph, output "1" if it contains a simple cycle (that is, a cycle which doesn’t intersect itself) of length 4 and "-1" otherwise.

#http://rosalind.info/problems/sq/

from sets import Set
from itertools import combinations
file="/Users/Mcfoofa/Downloads/rosalind_sq.txt"
lines = map(lambda x: x.rstrip(), list(open(file, "r")))
get_nums = lambda x: map(int, x.split())
n = get_nums(lines[0])
c=0
G={}
l=[]
results=[]
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
r=file_len(file)
def parse(l):
    c1=0
    for i in l:
        if c1>0:
            if i[0] not in G:
                G[i[0]]={i[1]}
            if i[1] not in G:
                G[i[1]]={i[0]}
            G[i[1]].add(i[0])
            G[i[0]].add(i[1])
        c1+=1
    sq(G)
def sq(G):
    for x, y in G.items():
        for a, b in combinations(y, 2):
            if G[a] & G[b] - {x}:  # check if sets intersection (minus the common vertex v) length > 0
                results.append(1)
                return
    results.append(-1)
    return

for i in range(r):
    if len(get_nums(lines[i]))>1:
         l.append(get_nums(lines[i]))
    if get_nums(lines[i])==[] and c>2:
        parse(l)
        G={}
        l=[]
    c+=1

for i in results:
    print i,
