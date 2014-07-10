d={"A":"U", "U":"A", "C":"G", "G":"C"} 
def split(x, y):
	c=0
	if not x and not y:
		print 1
	if x.count("A")==x.count("U") and x.count("G")==x.count("C"):
		if y.count("A")==y.count("U") and y.count("G")==y.count("C"):
			if x:
				for i in range(1, len(x)):
					if x[i]==d[x[0]]:
						split(x[1:i], x[i+1:])
			if y:
				for i in range(1, len(y)):
					if y[i]==d[y[0]]:
						split(y[1:i], y[i+1:])
		
def start(seq):
	c=0
	for i in range(1, len(seq)):
		if seq[i]==d[seq[0]]:
			split(seq[1:i], seq[i+1:])
start("GCAUGCAU")
