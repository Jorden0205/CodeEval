import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip().lower()
    	atoz = "abcdefghijklmnopqrstuvwxyz"

    	for t in list(test):
    		if t.isalpha():
    			atoz = atoz.replace(t,'')
    	if len(atoz) is 0:
    		print("NULL")
    	else:
    		print(atoz)