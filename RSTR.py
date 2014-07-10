s=87680
d="AAGTCTACAG"
cg=0.2134875
at=0.2865125
c=d.count("C")
a=d.count("A")
t=d.count("T")
g=d.count("G")
v=(cg**c)*(cg**g)*(at**a)*(at**t)
t=(1-v)**s
e=1-t
print e 
