import sys

with open(sys.argv[1], 'r') as test_cases:
	test_cases = test_cases.read().strip().splitlines()
	for test in test_cases:
		s, char = test.split(',')
		print(s.rfind(char))
