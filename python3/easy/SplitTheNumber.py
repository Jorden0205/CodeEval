import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split()
        nums = test[0]
        pattern = test[1]
        
        if '+' in pattern:
        	p = pattern.split('+')
        	first = int(nums[:len(p[0])])
        	sec = int(nums[len(p[0]):])
        	print( first + sec )
        elif '-' in pattern:
        	p = pattern.split('-')
        	first = int(nums[:len(p[0])])
        	sec = int(nums[len(p[0]):])
        	print( first - sec )


