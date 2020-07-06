#5번 가장 작은 곱
#1부터 20까지의 수로 전부 나눌 수 있는 수를 구하는 문제
#(1부터 20까지의 최소공배수를 구하는 문제)

import math

def M1T20():
	multi = 1
	for i in range(2, 21):
		multi *= i // math.gcd(i, multi)
	print(multi)