dict = {}
count = 0
for i in range(10):
    count +=1
    dict[count] = {int(input("Input roll no: ")), input("Name: "), int(input("Marks: ")), input("Grade: ")}

print(dict)