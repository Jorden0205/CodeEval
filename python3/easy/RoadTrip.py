import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.split(';')
		distances = []
		for t in test:
			info = t.strip().split(',')
			if len(info) != 2:
				continue
			distances.append(int(info[1]))
		distances = sorted(distances)
		
		result = ""
		result += str(distances[0])

		for i in range(0, len(distances) - 1):
			result += ',' + str(distances[i + 1] - distances[i])
		print(result)
