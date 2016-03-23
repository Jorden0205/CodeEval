import sys

with open(sys.argv[1], 'r') as test_cases:
    sum=0
    for test in test_cases:
        sum+=int(test)
        
    print(sum)