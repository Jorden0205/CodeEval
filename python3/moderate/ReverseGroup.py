import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(';')
        list_num = test[0].split(',')
        reverse_num = int(test[1])
        result = list()

        for i in range(0,len(list_num),reverse_num):
            if (len(list_num)-i) < reverse_num:
                result.extend(list_num[i: len(list_num)])
            else:
                result.extend(list_num[i: i+reverse_num][::-1])

        print(",".join(result))

