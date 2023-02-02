series = [0,1]
n = 9

for i in range(n-1):
    series.append(series[i]+series[i+1])

new_series = tuple(series)

print(new_series)

index = int(input("Enter the index: "))

print("The value corresponding to index",index,"is",new_series[index])