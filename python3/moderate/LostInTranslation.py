import sys

before = "rbc vjnmkf kd yxyqci na rbc zjkfoscdd ew rbc ujllmcptc rbkso rbyr ejp mysljylc kd kxveddknmc re jsicpdryside kr kd eoya kw aej icfkici re zjkr"
after = "the public is amazed by the quickness of the jugglerwe think that our language is impossible to understandso it is okay if you decided to quit"
codel = dict()

for i, b in enumerate(before):
	if b not in codel and b is not " ":
		codel[b] = after[i]

codel['g'] = 'v'
codel['h'] = 'x'

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	test = test.strip()
    	result = ""

    	for t in test:
    		if t in codel:
    			result += codel[t]
    		else:
    			result += t
    	print(result)