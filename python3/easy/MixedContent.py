import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(',')
        txt = list()
        num = list()
        result = ""
        for t in test:
            if t.isalpha():
                txt.append(t)
            else:
                num.append(t)

        result += ",".join(txt)
        if txt and num :
            result += "|"
        result += ",".join(num)
        print(result)
        
