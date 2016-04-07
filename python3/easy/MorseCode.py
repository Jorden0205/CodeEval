import sys

MORSECODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

INVERSECODE=dict((v,k) for (k,v) in MORSECODE.items())

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().split(" ")
        result = ""
        for t in test:
            if t is "":
                result += " "
            else:
                result += INVERSECODE[t]
        print(result)
