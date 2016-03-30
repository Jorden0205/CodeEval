import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(',')
        result = list()

        for t in test:
            if t not in result:
                result.append(t)
        print(",".join(result))