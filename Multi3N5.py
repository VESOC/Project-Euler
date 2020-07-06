#1번 3과 5의 배수
#1000 미만의 3과 5의 배수의 합을 구하는 문제 
#Find the sum of the multiples of 3 and 5 below 1000 (<1000)

def Multi3N5():
	sum3N5 = 0
	for i in range(1,1000): #Starts at 1, ends at 999
		if i % 3 == 0 or i % 5 == 0: #Check if i is a multiple of 3 or 5
			sum3N5 += i #If above statement is True, adds i to sum
	print(sum3N5)

#Using Set-Similar to Multi3N5
def Multi3N5MSet():
	ansSet = set()
	for i in range(1,1000):
		if i % 3 == 0 or i % 5 == 0:
			ansSet.add(i)
	print(sum(ansSet))

#Getting Each Mutiples of 3, 5, and 15
def getMutliple(n):
	ans = 999 // n
	return (ans * (ans+1)) // 2 * n
def Multi3N5M():
	print(getMutliple(3) + getMutliple(5) - getMutliple(15))