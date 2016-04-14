import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        angle = float(test)
        degree = int(angle)
        minutes = int((angle-degree)*60)
        seconds = int((angle-degree-(minutes/60))*3600)

        print(str(degree) + "." + str(minutes).rjust(2,'0') + "'" + str(seconds).rjust(2,'0') + '"')