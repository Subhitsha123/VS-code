import statistics

tup = eval(input("Enter the tuple: "))

sum_of_tup = sum(tup)

mean_1 = sum_of_tup/len(tup)

mean_2 = statistics.mean(tup)

print("The mean calculated with avg =",mean_1)
print("Mean calculated using statistics =",mean_2)