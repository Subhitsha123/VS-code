tup = eval(input("Enter the tuple: "))

for i in range(len(tup)):
        if tup[i][0]%2== 0 and tup[i][1]%2 == 0: 
            print(tup[i])