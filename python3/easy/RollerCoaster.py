import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = list(test)
        case = True
        for i, n in enumerate(test):
            if not n.isalpha():
                continue

            if case == 1:
                test[i] = n.upper()
            else:
                test[i] = n.lower()

            case = not case
            
        print("".join(test))
