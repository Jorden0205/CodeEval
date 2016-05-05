import sys

def reality(amount, largest=50):
	if amount == 0:
		return 1
	coins = [50, 25, 10, 5, 1]
	result = 0
	for c in coins:
		if c <= amount and c <= largest:
			result += reality( amount - c, c)
	return result

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = int(test.strip())
		print(reality(test))