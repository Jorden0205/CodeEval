import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split()
    	index = test[len(test)-1]
    	test.remove(index)
    	length = len(test)

    	if int(index) <= length:
    		print(test[length - int(index)])
