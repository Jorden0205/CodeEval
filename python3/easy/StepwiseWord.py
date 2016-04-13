import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split()
        longest = max(test, key=len)
        result = ""

        for i, t in enumerate(list(longest)):
        	stars = "".rjust(i, '*')
        	result += stars + t + " "
        print(result.strip())