import sys

hidden_dict = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = list(test.strip())
        result = ""
        for t in test:
            if t in hidden_dict:
                result += hidden_dict[t]
            elif t.isdigit():
                result += t
        if result != "":
            print(result)
        else:
            print("NONE")
