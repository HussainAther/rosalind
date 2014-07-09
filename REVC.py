def complement(text):
	new_text= ""
	for i in text:
		if i == "A":
			new_text+="T"
		elif i == "C":
			new_text+="G"
		elif i == "G":
			new_text+="C"
		else:
			new_text+="A"
	print new_text[::-1]
