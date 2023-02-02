num = eval(input("Enter the numerators list: "))
denum = eval(input("Enter the denominators list:"))

print("The given list of numerators is: ",num)
print("The given list of denominators is: ",denum)

lst = []

for i in range(len(num)):
    elements = num[i]/denum[i]
    lst.append(elements)

print("The Smallest fraction = ",num[lst.index(min(lst))],"/",denum[lst.index(min(lst))],sep = '')
print("The index of the smallest fraction = ",lst.index(min(lst)))