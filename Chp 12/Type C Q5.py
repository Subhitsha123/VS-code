stud_1 = eval(input("Enter the first student marks: "))
stud_2 = eval(input("Enter the second student marks: "))
stud_3 = eval(input("Enter the third student marks: "))
stud_4 = eval(input("Enter the fourth student marks: "))
stud_5 = eval(input("Enter the fifth student marks: "))

lst = []
lst.append(stud_1)
lst.append(stud_2)
lst.append(stud_3)
lst.append(stud_4)
lst.append(stud_5)
tup = tuple(lst)

print("The marks are",tup)