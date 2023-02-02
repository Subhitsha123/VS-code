print("Enter lists of the same size")
l = eval(input("Enter the list: "))
m = eval(input("Enter the list: "))
n = []

if len(l) == len(m):
    for i in range(len(l)):
        elements = l[i]+m[i]
        n.append(elements)

    print("List n: ",n)

else:
    print("Enter lists of the same size only!")