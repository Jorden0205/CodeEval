import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.split()
		for i,t in enumerate(test):
			end = len(t)-1
			t = list(t)
			if t[0] == t[end]:
				continue
			else:
				temp = t[0]
				t[0] = t[end]
				t[end] = temp
				test[i] = "".join(t)
		print(" ".join(test))

