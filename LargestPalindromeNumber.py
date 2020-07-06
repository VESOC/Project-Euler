#4번 가장 큰 회문인 곱
#세자리 수 두개를 곱해서 회문인 수 중 가장 큰 것을 구하는 문제 
def LPN():
	l = []
	for i in range(999, 99, -1):
		for j in range(999, 100, -1):
			n = str(i*j)
			if n == n[::-1]:
				l.append(int(n))
	print(max(l))

def LPNM2():
	l = 0
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			m = i*j
			n = str(m)
			if n == n[::-1] and m > l:
				l = m
	print(l)