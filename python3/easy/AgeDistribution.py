import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = int(test)
        if test in range(0,3):
            print("Still in Mama's arms")
        elif test in range(3,5):
            print("Preschool Maniac")
        elif test in range(5,12):
            print("Elementary school")
        elif test in range(12,15):
            print("Middle school")
        elif test in range(15,19):
            print("High school")
        elif test in range(19,23):
            print("College")
        elif test in range(23,66):
            print("Working for the man")
        elif test in range(66,100):
            print("The Golden Years")
        else:
            print("This program is for humans")