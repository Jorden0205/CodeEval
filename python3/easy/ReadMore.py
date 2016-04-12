import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip()
    	readmore = '... <Read More>'

    	if len(test) > 55:
    		test = test[:40]
    		if test.rfind(' ') != -1:
    			test = test[:test.rfind(' ')]
    		test += readmore

    	print(test)