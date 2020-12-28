def LCS():
	ans = [0]
	for i in range(1000000, 2, -1):
		cnt = 1
		j = i
		while j != 1:
			if j % 2:
				j = 3 * j + 1
			else:
				j //= 2
			cnt += 1
		if cnt >= ans[0]:
			ans = [cnt, i]
	print(ans[1])