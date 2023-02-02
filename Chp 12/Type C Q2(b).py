series = [0,1]
n = 9

for i in range(n-1):
    series.append(series[i]+series[i+1])

new_series = tuple(series)

print(new_series)

value = int(input("Enter the term in fibonacci series: "))

print(value,"is the",new_series.index(value)+1,"term")