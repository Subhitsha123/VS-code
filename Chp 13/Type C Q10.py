D1 = {'a':10,'b':20,'c':10}
D2 = {'a':10,'b':20,'c':30}
count = 0
lst = []

for keys in D1:
    lst.append(D1[keys])

for a in lst:
    if lst.count(a)>1:
        count = lst.count(a)

print(f'{count} keys have the same values')