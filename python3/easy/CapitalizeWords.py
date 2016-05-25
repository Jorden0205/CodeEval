import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = list(test.strip())
    	i = 0

    	while i < len(test):
    		if i == 0:
    			test[i] = test[i].upper()
    		elif test[i] == ' ':
    			test[i+1] = test[i+1].upper()
    			i += 1
    		i += 1
    	print("".join(test))