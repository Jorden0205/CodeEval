import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip()
    	test = "{0:b}".format(int(test))
    	print(test.count('1'))