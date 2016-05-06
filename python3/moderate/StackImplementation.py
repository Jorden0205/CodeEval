import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split(" ")[::-1]
    	result = ""
    	for i, t in enumerate(test):
    		if i%2 == 0:
    			result += t + " "
    		if t == " ":
    			count += 1
    	print(result.strip())