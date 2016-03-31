import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = list(test.strip())
        result = 1

        for i, n in enumerate(test):
            if test.count(str(i)) != int(n):
                result = 0
                break
        print(result)