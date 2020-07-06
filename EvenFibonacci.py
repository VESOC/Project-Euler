dp = [1, 2]
'''#Normal fibonacci recursion function using dynamic programming
def fibo(n):
	if n == 1:
		return dp[0]
	elif n == 2:
		return dp[1]
	else:
		tmp = fibo(n-1) + fibo(n-2)
		dp.append(tmp)
		return tmp'''

def fiboFor():
	for i in range(2, int(1e10)):
		dp.append(dp[i-1]+dp[i-2])
		if max(dp) >= 4e6:
			break
	sumi = 0
	for i in dp:
		if i % 2 == 0:
			sumi += i
	print(sumi)

def fiboWhile():
	Sum, tmp1, tmp2 = 0, 0, 1
	while tmp2 < 4000000:
		tmp2 += tmp1
		tmp1 = tmp2 - tmp1
		if tmp2 % 2 == 0:
			Sum += tmp2
	print(Sum)