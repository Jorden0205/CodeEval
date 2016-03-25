import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.split()
		num_zero = int(test[0])
		start = 1
		end = int(test[1])
		sum = 0

		list_range = list( bin(x) for x in range( start, end+1 ) )
		for l in list_range:
			if (l.count('0')-1) == num_zero:
				sum += 1
		print(sum)
