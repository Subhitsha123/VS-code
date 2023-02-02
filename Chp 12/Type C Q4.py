marks = eval(input("Enter marks: "))
list  =[]
roll_no = int(input("Enter the roll number: "))
name = input("Enter name: ")
tup = tuple(marks)

list.append(roll_no)
list.append(name)
list.append(marks)

new_tup = tuple(list)
print("The nested tuple is",new_tup)