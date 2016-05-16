import sys
import re

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
	    test = test.strip()
	    start = 0
	    count = 0

	    while start < len(test):
	    	start = test.find('<--<<', start)
	    	if start > -1:
	    		start += 4
	    		count += 1
	    	else:
	    		break
	    start = 0
	    while start < len(test):
	    	start = test.find('>>-->', start)
	    	if start > -1:
	    		start += 4
	    		count += 1
	    	else:
	    		break
	    print(count)