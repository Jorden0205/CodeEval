import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        if int(test) < 10:
            print(True)
            continue
        
        sum=0
        for t in test.strip():
            sum+=int(t) ** len(test)
        if sum == int(test):
            print(True)
        else:
            print(False)