# # Capitalize String
# # Python program to capitalize the first and last character of each word in a string (input string should be a statement)

name = input("Please provide a statement as input:")
name = name.title()
result = ""
for i in name.split():
    result = result + i[:-1] + i[-1].upper() + " "
print(result)
