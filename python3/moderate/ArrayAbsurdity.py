import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split(';')
    	nums = test[1].split(',')
    	d = {}

    	for n in nums:
    		if n not in d:
    			d[n]=True
    		else:
    			print(n)
    			break