lst = eval(input("Enter a list (numbers b/w 1 and 12): "))
print("The list input is",lst)

for i in range(0,len(lst)):
    if lst[i]>10:
        lst[i] = 10

print("The list after replacement is",lst)