#3번 가장 큰 소수인 약수
#600851475143의 가장 큰 소수인 약수를 구하는 문제 
import math
target = 600851475143

def smallest_Prime(n):
  for j in range(2, math.ceil(math.sqrt(n))):
    if n%j == 0:
      return j
  return n

def LPF():
	global target
	while True:
		n = smallest_Prime(target)
		if n < target:
			target //= n
		else:
			print(target)
			return 0

'''
target = 10
2*2 <= 10
2 !>= n
10%2==0
2 isPrime
10//2 = 5 = n
i = 3
3*3 < 10
3 !>= 5
5%3 != 0
i = 4
same as 3
i = 5

'''