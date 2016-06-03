import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().replace(" ", "")
    	total = 0

    	for i, t in enumerate(test):
    		if i%2 == 0:
    			total += int(t)*2
    		else:
    			total += int(t)

    	if total%10 == 0:
    		print("Real")
    	else:
    		print("Fake")