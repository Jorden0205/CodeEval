import sys

digit1 = '-**----*--***--***---*---****--**--****--**---**--'
digit2 = '*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-'
digit3 = '*--*---*---**---**--****-***--***----*---**---***-'
digit4 = '*--*---*--*-------*----*----*-*--*--*---*--*----*-'
digit5 = '-**---***-****-***-----*-***---**---*----**---**--'
digit6 = '--------------------------------------------------'

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.strip()

		result1 = ""
		result2 = ""
		result3 = ""
		result4 = ""
		result5 = ""
		result6 = ""

		for t in test:
			if t.isdigit():
				result1 += digit1[int(t)*5:int(t)*5+5]
				result2 += digit2[int(t)*5:int(t)*5+5]
				result3 += digit3[int(t)*5:int(t)*5+5]
				result4 += digit4[int(t)*5:int(t)*5+5]
				result5 += digit5[int(t)*5:int(t)*5+5]
				result6 += digit6[int(t)*5:int(t)*5+5]

		print(result1)
		print(result2)
		print(result3)
		print(result4)
		print(result5)
		print(result6)
