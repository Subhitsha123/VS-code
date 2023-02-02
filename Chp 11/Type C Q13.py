lst = eval(input("Enter the list: "))
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))

new_lst = lst[start:end+1]

print("Maximum Value =",max(new_lst))
print("Minimum Value =",min(new_lst))