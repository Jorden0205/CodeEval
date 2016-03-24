import sys
import re

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
	    result = re.findall('[a-zA-Z]+',test)
	    print(" ".join(result).lower())
