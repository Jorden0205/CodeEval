import sys

def is_happy(num, history=None):
    if history is None:
        history = []

    sum = 0
    for n in num:
        sum += int(n) ** 2

    if sum == 1:
        return 1
    elif sum in history:
        return 0
    else:
        history.append(sum)
        return is_happy(str(sum), history)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print(is_happy(test.strip()))