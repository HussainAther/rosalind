def rna_protein(s):
	s2=[ s[start:start+3] for start in range(0, len(s), 3) ]
	m=[ ]
	for item in s2:
		if item == "UUU":
			m.append("F")
		if item == "UUC":
			m.append("F")
		if item == "UUA":
			m.append("L")
		if item == "UUG":
			m.append("L")
		if item == "UCU":
			m.append("S")
		if item == "UCC":
			m.append("S")
		if item == "UCA":
			m.append("S")
		if item == "UCG":
			m.append("S")
		if item == "UAU":
			m.append("Y")
		if item == "UAC":
			m.append("Y")
		if item == "UAA":
			break
		if item == "UAG":
			break
		if item == "UGU":
			m.append("C")
		if item == "UGC":
			m.append("C")
		if item == "UGA":
			break
		if item == "UGG":
			m.append("W")
		if item == "CUU":
			m.append("L")
		if item == "CUC":
			m.append("L")
		if item == "CUA":
			m.append("L")
		if item == "CUG":
			m.append("L")
		if item == "CCU":
			m.append("P")
		if item == "CCC":
			m.append("P")
		if item == "CCA":
			m.append("P")
		if item == "CCG":
			m.append("P")
		if item == "CAU":
			m.append("H")
		if item == "CAC":
			m.append("H")
		if item == "CAA":
			m.append("Q")
		if item == "CAG":
			m.append("Q")
		if item == "CGU":
			m.append("R")
		if item == "CGC":
			m.append("R")
		if item == "CGA":
			m.append("R")
		if item == "CGG":
			m.append("R")
		if item == "AUU":
			m.append("I")
		if item == "AUC":
			m.append("I")
		if item == "AUA":
			m.append("I")
		if item == "AUG":
			m.append("M")
		if item == "ACU":
			m.append("T")
		if item == "ACC":
			m.append("T")
		if item == "ACA":
			m.append("T")
		if item == "ACG":
			m.append("T")
		if item == "AAU":
			m.append("N")
		if item == "AAC":
			m.append("N")
		if item == "AAA":
			m.append("K")
		if item == "AAG":
			m.append("K")
		if item == "AGU":
			m.append("S")
		if item == "AGC":
			m.append("S")
		if item == "AGA":
			m.append("R")
		if item == "AGG":
			m.append("R")
		if item == "GUU":
			m.append("V")
		if item == "GUC":
			m.append("V")
		if item == "GUA":
			m.append("V")
		if item == "GUG":
			m.append("V")
		if item == "GCU":
			m.append("A")
		if item == "GCC":
			m.append("A")
		if item == "GCA":
			m.append("A")
		if item == "GCG":
			m.append("A")
		if item == "GAU":
			m.append("D")
		if item == "GAC":
			m.append("D")
		if item == "GAA":
			m.append("E")
		if item == "GAG":
			m.append("E")
		if item == "GGU":
			m.append("G")
		if item == "GGC":
			m.append("G")
		if item == "GGA":
			m.append("G")
		if item == "GGG":
			m.append("G")
	print "".join(m)
	