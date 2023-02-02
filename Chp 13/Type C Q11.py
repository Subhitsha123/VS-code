d1 = eval(input("Enter dictionary 1: "))
d2 = eval(input("Enter dictionary 2: "))

y = 3
if len(d1)<len(d2):
    for key in d1:
        if key in d2:
            if d1[key] == d2[key]:
                y = 1

            else:
                y = 0

        else:
           y = 0 
           break 

    if y == 0:
        print("d1 is not contained in d2")

    elif y == 1:
        print("d1 is contained in d2")  

else:
    for key in d2:
        if key in d1:
            if d2[key] == d1[key]:
                y = 1

            else:
                y = 0
        else:
            y = 0
            break

    if y == 0:
        print("d2 is not contained in d1")

    elif y == 1:
        print("d2 is contained in d1")  