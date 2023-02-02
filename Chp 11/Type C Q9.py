lst = eval(input("Enter the list to be rotated: "))

print("Before rotation: ",lst)

lst.insert(0,lst[-1])  
lst.pop(-1)

print("After rotation: ",lst)