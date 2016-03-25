import sys
import json
with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		sum = 0
		test = json.loads(test)
		for t in test['menu']['items']:   
			if t != None and 'label' in t:
				sum += int(t['id'])
		print(sum)
