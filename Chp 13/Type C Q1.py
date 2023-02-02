dict = {}
ans = 'y'

while ans == 'y':
    employees, salaries = eval(input("Enter employees, salries: "))
    dict[employees] = salaries

    ans = input("More employees?(y/n)")

print(dict)