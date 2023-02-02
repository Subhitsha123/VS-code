string = input("Enter the string: ")
dict=  {}

for i in string:
    if i not in dict:
        dict[i] = string.count(i)

print("The count of characters is",dict)