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

print("The total marks of student 1",sum(stud_1))
print("The total marks of student 2",sum(stud_2))
print("The total marks of student 3",sum(stud_3))
print("The total marks of student 4",sum(stud_4))
print("The total marks of student 5",sum(stud_5))

print("The average marks of student 1",sum(stud_1)/5)
print("The average marks of student 2",sum(stud_2)/5)
print("The average marks of student 3",sum(stud_3)/5)
print("The average marks of student 4",sum(stud_4)/5)
print("The average marks of student 5",sum(stud_5)/5)


