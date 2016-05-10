import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split()
    	counter = [[x, test.count(x)] for x in test]
    	lowest = 0
    	player = 0
    	i = 0
    	for x, y in counter:
    		i += 1
    		if y == 1:
    			if lowest == 0 or lowest > int(x):
    				lowest = int(x)
    				player = i
    	print(player)
