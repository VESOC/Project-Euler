ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
tenones = ['ten', 'eleven', 'twelve', 'thriteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def under100(i):
	if i < 20:
		if i < 10:
			return ones[i]
		else:
			return tenones[i-10]
	else:
		j = [int(k) for k in str(i)]
		return tens[j[0]] + ones[j[1]]

def NLC():
	s = ''
	for i in range(1, 1001):
		if i < 100:
			s += under100(i)
		elif i < 1000:
			s += ones[i//100] + 'hundred' + ('and' + under100(i%100) if i % 100 != 0 else '')
		else:
			s += ones[i//1000] + 'thousand'
	print(len(s))