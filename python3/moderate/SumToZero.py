import sys
import itertools

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = map(int,test.strip().split(','))
        combinations = [list(x) for x in itertools.combinations(test,4)]
        result = 0
        for c in combinations:
            if sum(c) == 0:
                result += 1
        print(result)