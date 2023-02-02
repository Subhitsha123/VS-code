
fee = {'B': 300, 'I': 450, 'A': 600}
fee['S'] = 1200

level = input("Enter the level: ")

if level not in fee:
    print("Not a valid level")

else:
    lessons = int(input("Enter the number of lessons: "))
    print((fee[level])*lessons)

print(sorted(fee.items()))
print(max(fee.values()))