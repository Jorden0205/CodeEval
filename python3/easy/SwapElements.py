import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split(':')
        numbers = test[0].split()
        swaps = test[1].split(',')

        for swap in swaps:
        	swap = swap.split('-')
        	s1 = int(swap[0])
        	s2 = int(swap[1])
        	temp = numbers[s1]
        	numbers[s1] = numbers[s2]
        	numbers[s2] = temp
        print(" ".join(numbers))
