#10번 소수들의 합
#2백만보다 작은 소수들의 합을 구하시오

l = [i for i in range(2000001)]

def SOP():
	for i in range(2, 2000001):
		if l[i] != 0:
			for j in range(i+i, 2000001, i):
				if j < len(l):
					l[j] = 0
	n = set()
	for i in l:
		if i not in (0, 1) and i < 2000000:
			n.add(i)
	print(sum(n))