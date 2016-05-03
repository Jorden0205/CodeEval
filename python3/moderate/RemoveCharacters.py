import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split(',')
    	string = test[0].strip()
    	scrub = test[1].strip()

    	for s in scrub:
    		string = string.replace(s,'')

    	print(string)