def LPN():
	l = []
	for i in range(999, 99, -1):
		for j in range(999, 100, -1):
			n = str(i*j)
			if n == n[::-1]:
				l.append(int(n))
	print(max(l))

