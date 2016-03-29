import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(",")
        half_len = len(test)/2
        result = None
        counter = dict()

        for t in test:
            if t in counter:
                counter[t] += 1
            else:
                counter[t] = 1
            if counter[t] > half_len:
                result = t
                break
        print(result)
