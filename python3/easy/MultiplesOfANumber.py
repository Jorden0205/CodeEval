import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.strip().split(',')
		x = int(test[0])
		n = int(test[1])
		sum = 0
		while sum<x:
			sum+=n
		print(sum)