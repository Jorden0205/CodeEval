import sys
import re

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if test == "":
            continue

        test = test.strip().lower()

        match = re.match('^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}', test)

        if match == None:
            print("false")
        else:
            print("true")
