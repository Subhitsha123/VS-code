lst_1 = eval(input("Enter the first list: "))
lst_2 = eval(input("Enter the second list: "))

if lst_1 == lst_2:
    print("The lists do not differ")

elif len(lst_1) == len(lst_2):
    for i in range(len(lst_1)):
        if lst_1[i] != lst_2[i]:
            break
    print("The index at which the lists differ = ",i)

else:
    print("Enter lists of same size only!")