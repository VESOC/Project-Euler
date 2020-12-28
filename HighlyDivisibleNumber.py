import math

def HDN():
	count, j, n, l = 0, 0, 1, 0
	while count < 500:
		count = 0
		l += n
		for i in range(1, math.ceil(math.sqrt(l))):
			if l % i == 0:
				count += 2
			j = i
		if j*j == l:
			count -= 1
		n += 1
	print(l)