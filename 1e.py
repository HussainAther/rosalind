s="GTAAGTTAGTTCACACAATAAGGATTCTCATGCTTTATAGAGAGGTGCATCTCTGTTAT"
t=[ ]
for i in range(len(s)):
	a=s[:i].count("C")
	b=s[:i].count("G")
	t.append(b-a)
e=min(t)
for r in range(len(t)):
	if t[r]==e:
		print r,