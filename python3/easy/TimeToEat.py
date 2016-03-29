import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.split()
		sort = sorted(test, reverse=True)
		print(" ".join(sort))
