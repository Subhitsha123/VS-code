tup = eval(input("Enter a tuple of string = "))
if tup == () :
    print("Tuple should contain at least one element ")
else :
    shortest = tup[0]
    for i in range(len(tup)) :
        if len(shortest) < len(tup[i]) :
            shortest = shortest
    print("Length of shortest string in list =",len(shortest))