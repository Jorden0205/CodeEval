import sys

num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
			'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
	    test = test.strip().split(';')
	    result = ""

	    for t in test:
	    	result += num_dict[t]

	    print(result)

