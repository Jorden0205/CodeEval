import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split('|')
        first = test[0].split()
        second = test[1].split()

        for i, v in enumerate(first):
            first[i] = str(int(first[i]) * int(second[i]))

        print(" ".join(first))