lst = eval(input("Enter the list containing strings with at least 1 element: "))
print("The given list is: ",lst)

if lst!=[]:
    print("The longest string of the given list is", max(lst ,key = len))

else:
    print("The list must contain at least 1 element! ")
    

