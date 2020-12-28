#2번 짝수 피보나치 수열
#4백만을 넘지 않는 피보나치 수열의 짝수 항들의 합을 구하는 문제 

dp = [1, 1]
'''#Normal fibonacci recursion function using dynamic programming
dp = [];
def fibRecursiveMem(n):
    if (dp[n]):
			 return dp[n];
    if (n<=2):
			 dp[n] = 1
    else:
        dp[n] = fibRecursiveMem(n-1) + fibRecursiveMem(n-2)
    return dp[n]
'''

def fiboRecur():
	i = 2
	while dp[i-1] <= 4e6:
		dp.append(dp[i-1]+dp[i-2])
		i += 1
	print(sum(dp[2::3]))

def fiboRep():
	Sum, tmp1, tmp2 = 0, 1, 2
	while tmp2 <= 4000000:
		if tmp2 % 2 == 0:
			Sum += tmp2
		tmp1, tmp2 = tmp2, tmp1 + tmp2
	print(Sum)

	