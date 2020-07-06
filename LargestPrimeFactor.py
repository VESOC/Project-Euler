target = 600851475143

def ifPrime(n):
  for j in range(2, n):
    if n%j == 0:
      return False
  return True

def LPF():
	i = 2
	n = target
	while i*i <= target:
		if i >= n:
			print(i)
			return 0
		if n % i == 0:
			if ifPrime(i):
				n //= i
		i += 1