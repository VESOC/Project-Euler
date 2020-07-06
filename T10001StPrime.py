#7번 10001번째 소수
#10001번째 소수를 구하는 문제

def ifPrime(n):
  for j in range(2, n):
    if n%j == 0:
      return False
  return True

def T10001StPrime():
	i, n = 0, 2
	while i != 10001:
		if ifPrime(n):
			i += 1
		n += 1
	print(n-1)

#에라토스테네스의 체
l = [i for i in range(200001)]

def EP():
	for i in range(2, 200001):
		if l[i] != 0:
			for j in range(i+i, 200001, i):
				l[j] = 0
	n = []
	for i in l:
		if i not in (0, 1):
			n.append(i)
	print(n[10000])