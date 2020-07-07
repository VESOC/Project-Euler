#20번 100!의 각 자릿수의 합
# 100!의 각 자릿수의 합을 구하는 문제

import math

def FDS():
	ans = 1
	for i in range(2, 101):
		ans *= i
	print(sum(int(i) for i in str(ans)))

def FDSM2():
	print(sum(int(i) for i in str(math.factorial(100))))