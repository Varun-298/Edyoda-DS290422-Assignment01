name = input("Please provide a statement as input:")
count = 0
if name.__contains__("a"): 
    count = count + name.count("a")
if name.__contains__("e"):
    count = count + name.count("e")
if name.__contains__("i"): 
    count = count + name.count("i")
if name.__contains__("o"):
    count = count + name.count("o")
if name.__contains__("u"): 
    count = count + name.count("u")
else:
    print('no vowels found')
    
print("Total vowels count:",count)


