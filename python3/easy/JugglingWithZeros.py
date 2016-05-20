import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split(' ')
    	result = ""

    	n = 0
    	while n < len(test):
    		if test[n] == '00':
    			result += test[n+1].replace('0','1')
    		elif test[n] == "0":
    			result += test[n+1]
    		n += 2

    	print( int(result,2))