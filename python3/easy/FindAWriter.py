import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
	    test = test.strip().split('|')
	    name = list(test[0])
	    keys = test[1].split()
	    result = ""

	    for k in keys:
	    	result += name[int(k)-1]

	    print(result)

