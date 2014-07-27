f=open("/Users/Mcfoofa/Downloads/2sumsample.txt", "r")
c=""
b=""
l=[]
for i in f.readlines():	
	c+=i
def func(i):
    a=0
    d=""
    for j in enumerate(i.split(" "), -1):
        for k in enumerate(i.split(" "), -1):
            if k[1][-1]==j[1][-1]:
                if int(j[1])==int(k[1])*-1:
                    d=(str(int(j[0])+2)+" "+str(int(k[0]+2)))
                    print d
        if d!="":
            print d
            return
    print "-1"
for i in c.split("\n"):
    func(i)
