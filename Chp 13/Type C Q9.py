D1 = eval(input("Enter Dictionary 1: "))
D2 = eval(input("Enter Dictionary 2: "))

lst = []

for key in D1:
    if key in D2:
        lst.append(key)

print(lst)