import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split(',')
    	num = str(bin(int(test[0])))[2:]
    	p1 = int(test[1])-1
    	p2 = int(test[2])-1
    	result = str(num[::-1][p1] == num[::-1][p2]).lower()
    	print(result)
