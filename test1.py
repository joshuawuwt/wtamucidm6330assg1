# import int_to_roman from int2roman

# test #1: invalid letter
romanletters = ["I", "V", "X", "L", "C", "D", "M"]
output = "MXXVI" # will replace with the convertion function.
invalidletters = []
for letter in output:
    if letter not in romanletters:
        invalidletters.append(letter)
        print(f"Error 0001 : {invalidletters} is not an invalid roman letter") 
    else:
        print("test #1 pass - no invalid letter found")

