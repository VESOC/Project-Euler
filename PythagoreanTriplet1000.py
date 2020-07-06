#9번 특별한 피타고라스 수
#합이 1000을 이루는 피타고라스 수들의 곱을 구하는 문제

def PTT():
	for a in range(3, 988):
		for b in range(4, 988):
			c = 1000 - a - b
			if a*a + b*b == c*c:
				print(a*b*c)
				return 0