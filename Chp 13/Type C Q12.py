D1 = eval(input("Enter the dictionary: "))
D2 = {}

for keys in D1:
    D2[keys] = sum(D1[keys])

print(D2)