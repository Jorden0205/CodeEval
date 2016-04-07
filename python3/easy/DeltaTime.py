import sys
from datetime import datetime
import time

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.strip().split()
		test = sorted(test)
		s1 = test[0]
		s2 = test[1]
		FMT = '%H:%M:%S'
		tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
		tdelta = int(tdelta.total_seconds())
		print(time.strftime(FMT,time.gmtime(tdelta)))
		
