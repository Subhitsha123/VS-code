lst = eval(input("Input the list: "))
num = int(input("Enter the number to be checked: "))

print("The given list is",lst)
print("The number to be checked is",num)

if num in lst:
    print("The number is in the list")
    print("The position by index of the number is",lst.index(num))

else:
    print("The number is not in the list")