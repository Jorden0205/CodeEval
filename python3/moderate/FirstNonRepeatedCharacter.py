import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = list(test.strip())
    	result = ""

    	for t in test:
    		if test.count(t) == 1:
    			result = t
    			break
    	print(result)