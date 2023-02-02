dict = {'January': 31, 'February': 28, 'March': 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "Decmeber":31}
new_dict = {}

month = input("Enter month name: ")
print(f"Number of days in {month} is {dict[month]}.")

lst = []
for key in dict:
    lst.append(key)
    lst.sort()

print("Months in alphabetical order is",lst)

for key in dict:
    if dict[key] == 31:
        print(key, end = ',')

sorted = sorted(dict.values())
print()

for val in sorted:    
    for keys in dict:
        if val == dict[keys]:
            new_dict[keys] = val

print(new_dict)