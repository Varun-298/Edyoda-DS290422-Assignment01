#Special Characters
# Program to check if a string contains any special character.

name = input("Please provide an input:")
result = ""
for i in name.split():
    result = result + i
is_alpha = result.isalpha() 
if is_alpha == True:
    print("String is accepted ")
else:
    print("String is not accepted ")
    