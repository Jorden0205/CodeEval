import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:

    	if test == "":
    		continue

    	test = test.strip().split(",")

    	str1 = test[0]
    	str2 = test[1]

    	print( int( str1[len(str1)-len(str2):] == str2 ))