import sys
import re

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = re.findall('[a-z]+',test.lower())
        test = "".join(test)
        max_beauty = 26
        sum = 0
        counter = {}
        for t in test:
            if t in counter:
                counter[t] += 1
            else:
                counter[t] = 1

        while len(counter)>0:
            maxkey = max(counter, key=counter.get)
            sum += counter[maxkey] * max_beauty
            counter.pop(maxkey, None)
            max_beauty-=1
            
        print(sum)
