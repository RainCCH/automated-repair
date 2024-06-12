for i in range(int(input())):
	number = int(input())
	list = [2**i for i in range(33)]
	answer = []
	for i in list:
		if i <=list[i]:
			answer.append(i)
		else:
			answer.append(0)
	print(''.join(answer))