import sys
import re

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split(',')
    	print(test[0] in (test[1]+test[1]))