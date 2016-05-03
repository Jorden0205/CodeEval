import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.strip().split(',')
		max_ending_here = max_so_far = int(test[0])
		for x in test[1:]:
			x = int(x)
			max_ending_here = max(x, max_ending_here + x)
			max_so_far = max(max_so_far, max_ending_here)

		print(max_so_far)