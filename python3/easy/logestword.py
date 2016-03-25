import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.split()
		result = ""
		for t in test:
			if len(t) > len(result):
				result = t
		print(result)