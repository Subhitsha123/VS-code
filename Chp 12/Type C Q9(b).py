lst = []

for i in range(1,27):
    lst.append(chr(96+i)*i)

tup = tuple(lst)

print("The required tuple is",tup)