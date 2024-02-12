

convertion =[ 
    ["", "M", "MM", "MMM"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
]




def int2roman(x):
    digits = [1000, 100, 10, 1]
    i = 0
    
    output = ""
    for d in digits:
        y = x // d
        x %= d
        output += convertion[i][y]
        i += 1
    print(output)

input = int(input("Enter a integer between 1 and 3999:"))    
int2roman(input)

# step 1 convert integer to digital


# step 2 convert 

# length = len(string)

# numbers = [0, 0, 0, 0]
# i = -1
# roman = ""
# for l in string:
#     numbers[i] = int(string[i])
#     roman = convertion[i+4][numbers[i+4]] + roman
#     i -= 1

# # roman = convertion[0][numbers[0]] + convertion[1][numbers[1]] + convertion[2][numbers[2]] + convertion[3][numbers[3]]

# print(roman)