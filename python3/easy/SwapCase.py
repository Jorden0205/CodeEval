import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = list(test)
        for i, n in enumerate(test):
            if n.isupper():
                test[i] = n.lower()
            else:
                test[i] = n.upper()
        print("".join(test))
