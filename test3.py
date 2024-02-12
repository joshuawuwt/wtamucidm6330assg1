# import int_to_roman from int2roman

# test #3: identical test

# step 1 convert the special letter combinations.
output = "CDIV" # will replace with the convertion function.
specialletters = {"IV":"IIII", "IX":"VIIII", "XL":"XXXX", "XC":"LXXXX", "CD":"CCCC", "CM":"DXXXX"}

for letter in specialletters:
    if letter in output:
       output = output.replace(letter, specialletters[letter])
       

print(output)        

# step 2 convert step 1 result to integer

roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

i = 0

for letter in output:
    i += roman[letter]

print(i)


# length = len(string)
# convertion =[ 
#     ["", "M", "MM", "MMM"],
#     ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
#     ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
#     ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
# ]
# numbers = [0, 0, 0, 0]
# i = -1
# roman = ""
# for l in string:
#     numbers[i] = int(string[i])
#     roman = convertion[i+4][numbers[i+4]] + roman
#     i -= 1

# # roman = convertion[0][numbers[0]] + convertion[1][numbers[1]] + convertion[2][numbers[2]] + convertion[3][numbers[3]]

# print(roman)