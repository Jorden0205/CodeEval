import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip()
    	print( (int(test)+1)%2 )