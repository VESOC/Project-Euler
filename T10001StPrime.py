def ifPrime(n):
  for j in range(2, n):
    if n%j == 0:
      return False
  return True

def T10001StPrime():
	i, n = 0, 2
	while i != 10001:
		if ifPrime(n):
			#print(n)
			i += 1
		n += 1
	print(n-1)

l = [i for i in range(2000001)]
def EP():
	for i in range(2, 2000001):
		if i != 0:
			for j in range(i+i, 2000001, i):
				if j < len(l):
					l[j] = 0
	n = []
	for i in l:
		if i != 0:
			n.append(i)
	print(n[100001])