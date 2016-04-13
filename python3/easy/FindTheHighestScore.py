import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split('|')
        result = []
        for t in test:
        	scores = t.strip().split(" ")
        	for i, s in enumerate(scores):
        		if len(result) is not len(scores):
        			result.append(s)
        		elif int(s) > int(result[i]):
        			result[i] = s
        print(" ".join(result))
