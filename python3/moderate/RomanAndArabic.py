import sys

roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = list(test.strip())
    	result = 0
    	i = 0
    	temp = 1000

    	while i < len(test):
    		num = test[i]
    		roman_num = roman[ test[i+1] ]
    		
    		if roman_num > temp:
    			result -= int(test[i-2]) * roman[ test[i-1] ] * 2
    			
    		result += int(num) * roman_num
    		temp = roman_num
    		i += 2
    	print(result)