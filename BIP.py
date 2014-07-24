###################################
#A bipartite graph is a graph G=(V,E) whose vertices can be partitioned into two sets (V=V1∪V2 and V1∩V2=∅) such that there are no edges between vertices in the same set (for instance, if u,v∈V1, then there is no edge between u and v).

#There are many other ways to formulate this property. For instance, an undirected graph is bipartite if and only if it can be colored with just two colors. Another one: an undirected graph is bipartite if and only if it contains no cycles of odd length.

#Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

#Given: A positive integer k≤20 and k simple graphs in the edge list format with at most 103 vertices each.

#Return: For each graph, output "1" if it is bipartite and "-1" otherwise.

#See Figure 1 for visual example from the sample dataset.

#http://rosalind.info/problems/bip/
#############################################
f=open("/Users/Mcfoofa/Downloads/rosalind_bip-4.txt", "r")
c=1
r=0
d=0
result=[]
def color(x, y, q, z):
	q1=[]
	for i in q:
		if x[i]:
			for j in x[i].split(" "):
				if y[int(j)]==-1 and y[int(i)]==0:
					y[int(j)]=1
					q1.append(int(j))
				elif y[int(j)]==-1 and y[int(i)]==1:
					y[int(j)]=0
					q1.append(int(j))
				z[int(i)]=1
	for i in z:
		if z[i]==0:
			q1.append(i)	
	#print y
	#print z
	if q1:
		color(x, y, q1, z)
	return y
def check(x, y):
	#print y
	for i in x:
		if x[i]:
			for j in x[i].split(" "):
				if y[int(j)]==1 and y[int(i)]==1:
					return "-1"
				if y[int(j)]==0 and y[int(i)]==0:
					return "-1"
	return					
def bi(x, y):
	count=len(x)
	q=[]
	z={}
	#print x
	#print y
	for i in x:
		if x[i]:
			for j in x[i].split(" "):
				if y[int(j)]==-1:
					y[int(j)]=0
					q.append(int(j))
			break
	count=0
	for i in x:
		if x[i]:
			z[i]=0
	y=color(x, y, q, z)
# 	else:
# 		result.append("-1")
# 		return
	if check(x, y)=="-1":
		result.append("-1")
		return
	#print y
	result.append("1")
	return
for i in f.readlines():
	if len(i)>1 and c>0:
		if c==1:
			d={y: "" for y in range(1, int(i.split()[0])+1)}
			e={y: -1 for y in range(1, int(i.split()[0])+1)}
		elif c>1:
			q=str(int(i.split()[0]))
			r=str(int(i.split()[1]))
			if d[int(q)] and str(r) not in d[int(q)]:
				d[int(q)]+=" "+str(r)
			else:
				d[int(q)]=r
			if d[int(r)] and str(q) not in d[int(r)]:
				d[int(r)]+=" "+str(q)
			else:
				d[int(r)]=q
	else:
		#print d
		bi(d, e)
		c=0
	c+=1
for i in result:
	print i,
