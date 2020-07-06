import math

def M1T20():
	multi = 1
	for i in range(2, 21):
		multi *= i // math.gcd(i, multi)
	print(multi)