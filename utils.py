from typing import List

roman_number_codes = {
    "I" : 1,
    "IV" : 4,
    "V" : 5,
    "IX" : 9,
    "X" : 10,
    "XL" : 40,
    "L" : 50,
    "XC" : 90,
    "C" : 100,
    "CD" : 400,
    "D" : 500,
    "CM" : 900,
    "M" : 1000
}

def dictArrayCombine(d : List[dict]) -> dict:
    newDict = dict()
    for x in d:
        for k, v in x.items():
            newDict[k] = v
    return newDict

def simpleToRoman(i : int) -> str:
    s = ""

    x = len(roman_number_codes) - 1
    while x > 0:
        x -= 1
        ri = list(roman_number_codes.items())
        s += ri[x][0] * ( i // ri[x][1])
        i -= (i // ri[x][1]) * ri[x][1]
        
    return s
