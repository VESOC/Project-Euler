#Find the sum of the multiples of 3 and 5 below 1000 (<1000)

def Multi3N5():
	sum3N5 = 0
	for i in range(1,1000): #Starts at 1, ends at 999
		if i % 3 == 0 or i % 5 == 0: #Check if i is a multiple of 3 or 5
			sum3N5 += i #If above statement is True, adds i to sum
	print(sum3N5)

#Getting the answer by sequence/mathematics
target = 999
def getMutliple(n):
	divideByN = target // n
	return (divideByN * (divideByN+1)) // 2 * n
def Multi3N5M2():
	print(getMutliple(3)+getMutliple(5)-getMutliple(15))

#Using Set-Similar to Multi3N5
def Multi3N5MSet():
	ansSet = set()
	for i in range(1,1000):
		if i % 3 == 0 or i % 5 == 0:
			ansSet.add(i)
	print(sum(ansSet))