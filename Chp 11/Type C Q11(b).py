lst = eval(input("Enter the list: "))
L = int(input("Enter the number to be added to each element: "))
new_list = []

for i in range(len(lst)):
    elements = lst[i]+L
    new_list.append(elements)

print("The final list after adding L is:",new_list)