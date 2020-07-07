#2번 짝수 피보나치 수열
#4백만을 넘지 않는 피보나치 수열의 짝수 항들의 합을 구하는 문제 

dp = [1, 1, 2]
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

def fiboRecur():
	i = 3
	while dp[i-1] <= 4e6:
		dp.append(dp[i-1]+dp[i-2])
		i += 1
	print(sum(dp[2::3]))
	print(dp)

def fiboRep():
	Sum, tmp1, tmp2 = 0, 0, 1
	while tmp2 < 4000000:
		tmp1, tmp2 = tmp2, tmp1 + tmp2
		if tmp2 % 2 == 0:
			Sum += tmp2
	print(Sum)