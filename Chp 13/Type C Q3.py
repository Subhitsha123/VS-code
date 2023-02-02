dict = {0:'Zero ',1:'One ',2:'Two ',3:'Three ',4:'Four ',5:'Five ',6:'Six ',7:'Seven ',8:'Eight ',9:'Nine '}

num = str(int(input("Enter the number: ")))

new_str = ""

for i in num:
    new_str += dict[int(i)]

print("Number in words is",new_str)