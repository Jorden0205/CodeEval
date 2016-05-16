import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split('|')
    	dev = test[0].strip()
    	design = test[1].strip()
    	result = 0

    	for i, d in enumerate(dev):
    		if len(design)-1 < i or d != design[i]:
    			result += 1

    	if result == 0:
    		print("Done")
    	elif result <= 2:
    		print("Low")
    	elif result <= 4:
    		print("Medium")
    	elif result <= 6:
    		print("High")
    	else:
    		print("Critical")