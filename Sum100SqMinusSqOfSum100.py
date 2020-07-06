def SHSMSSH():
	SumOf100Sq = 0
	for i in range(1, 101):
		SumOf100Sq += i ** 2
	SqOfSum100 = sum(i for i in range(1, 101)) ** 2
	print(SqOfSum100 - SumOf100Sq)