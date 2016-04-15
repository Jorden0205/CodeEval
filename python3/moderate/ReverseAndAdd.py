import sys

def palindrome(number):
	mid = int(len(number)/2)
	if len(number) % 2 != 0:
		return number[:mid] == number[mid+1:][::-1]
	else:
		return number[:mid] == number[mid:][::-1]

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip()
    	times = 0
    	result = test

    	while palindrome(result) is False:
    		result = str( int(result) + int( result[::-1]) )
    		times += 1
    	print(str(times) + " " + result)