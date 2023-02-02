n = int(input("How many number: "))
list = []

while n>0:
    num = int(input("Enter the numbers: "))
    list.append(num)
    n-=1

print(list)

tup = tuple(list)

print("The tuple is",tup)

print("The maximum number is",max(tup))