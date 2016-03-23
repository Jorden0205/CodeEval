import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split()
        txt = list(test[0])
        bin = test[1]

        for i, b in enumerate(bin):
            if b == '1':
                txt[i] = txt[i].upper()

    print("".join(txt))
