lst = eval(input("Enter a list of string: "))
print("The given list is",lst)

for i in range(len(lst)):
    lst[i] = lst[i][1:]

print("The list with the first characters removed is",lst)


