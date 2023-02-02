lst = eval(input("Enter the list: "))
num = int(input("Enter the number by which elements are to be incremented: "))

print("Before incremenation: ",lst)
for a in range(0,len(lst)):
    lst[a] = lst[a]+num

print("After incremenation: ",lst)