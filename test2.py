# import int_to_roman from int2roman

# test #2: non-repeated letter rule
output = "CCCCXVVV" # will replace with the convertion function.
nreletters = ["VV", "LL", "DD", "IIII", "XXXX", "CCCC", "MMMM"]

for letter in nreletters:
    if letter in output:
        print(f"Error 0002 : {letter} violate the repeated rule")
    else:
        print(f"test #2 pass - The repeated rule is compliant")

