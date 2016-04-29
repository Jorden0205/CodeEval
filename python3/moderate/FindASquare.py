import sys
import math

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        points = sorted(eval(test))
        result = 'false'
        if len(points) == 4:
            centx = sum( i[0] for i in points)/4
            centy = sum( i[1] for i in points)/4
            result = False

            circlefunc = { math.sqrt(math.fabs(x - centx)) + math.sqrt(math.fabs(y - centy)) for x, y in points}
            result = ('false', 'true')[len(circlefunc) == 1 and next(iter(circlefunc)) > 0]
        print(result)