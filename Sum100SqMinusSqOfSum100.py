#6번 제곱수 빼기 합의 제곱
#1부터 100까지의 수의 제곱수의 합과 1부터 100까지의 합의 제곱수의 차를 구하는 문제

def SHSMSSH():
	SumOf100Sq = 0
	for i in range(1, 101):
		SumOf100Sq += i ** 2
	SqOfSum100 = sum(i for i in range(1, 101)) ** 2
	print(SqOfSum100 - SumOf100Sq)