import sys
import math

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().split()
    	lower = 0
    	upper = int(test[0])
    	test.remove(test[0])

    	for t in test:
    		mid = math.ceil((upper + lower)/2)
    		if t == "Lower":
    			upper = mid-1
    		elif t == "Higher":
    			lower = mid+1
    		else:
    			break
    	print(mid)
