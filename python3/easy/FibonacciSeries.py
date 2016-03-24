import sys

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)
        
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	print(fibonacci(int(test.strip())))

