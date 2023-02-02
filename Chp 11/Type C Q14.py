lst = eval(input("Enter the list: "))

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            lst.append(lst.pop(lst.index(lst[i])))

print(lst)