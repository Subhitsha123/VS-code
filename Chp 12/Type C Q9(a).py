lst = []

for i in range(1,51):
    lst.append(i**2)

tup = tuple(lst)

print("The square of integers 1 through 50 is",tup)