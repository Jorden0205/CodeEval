import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = list(test.strip())
		length = len(test)
		upper = 0

		for t in test:
			if t.isupper():
				upper += 1

		print( "lowercase: %.2f uppercase: %.2f" % ((length-upper)/length*100,upper/length*100) )