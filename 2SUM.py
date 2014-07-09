f=open("/Users/Mcfoofa/Downloads/2sumsample.txt", "r")
c=""
b=""
l=[]
for i in f.readlines():	
	c+=i
def func(i):
	a=0
	for j in enumerate(i.split(" ")):
		if a==1:
			return
		for k in enumerate(i.split(" ")):
			if k[1][-1]==j[1][-1]:
				if int(j[1])==int(k[1])*-1:
					print str(int(j[0])+1)+" "+ str(int(k[0]+1))
# 					print str(int(k[0])+1) + "number" + str(int(k[1]))
					return 
					a+=1
	if a==0:
		print "-1"
for i in c.split("\n"):
	func(i)

#  should i add  "and int(j[1])!=int(0)" to exclude zeroes from the matching?