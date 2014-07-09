import itertools
f=open("/Users/Mcfoofa/Downloads/rosalind-bfs.txt", "r")
n=6
l={}
for i in range(1,n+1):
	l[i]=""
for i in f.readlines():
	l[int(i.split(" ")[0].replace("\n", ""))]+=str(i.split(" ")[1].replace("\n", ""))
print l
# out=[combo for combo in itertools.permutations(l,2)]
# for i in out:
# 	if i[0].startswith("0"):
# 		print i
# for i in range(1, 7):
# 	check(i)
# def check(e):
# 	p=0
# 	if e!=1:
# 		for j in range(1,e):
# 			for u in l:	
# 				if u[0]==j:
# 					p+=1
def check(i, p, l):
	for e in l:	
		if l[e]:
			if str(i) in l[e]:
				p+=1
				check(i+1, p, l)
		elif l[e][2]==i:
			print p
for i in range(2, n+1):	
	for j in l:
		if l[j]:
			if str(i) in l[j]:
				p=0
				check(i+1, p, l)
			else:
				print 0
