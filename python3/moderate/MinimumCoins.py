import sys

def countcoin(num, coin):
	usedcoins = int(num/coin)
	if usedcoins > 0:
		return (usedcoins, num-coin*usedcoins)
	else:
		return (0, num)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = int(test.strip())
    	coin = [5, 3, 1]
    	result = 0
    	for c in coin:

    		if test == 0:
    			break
    		used, test = countcoin(test,c)
    		result += used
    	print(result)