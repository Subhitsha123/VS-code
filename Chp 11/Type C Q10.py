series = [0,1]
n = int(input("Enter n(0 to 20): "))

for i in range(n-1):
    series.append(series[i]+series[i+1])

print(series)
value = series[len(series)-1]

print("The value of the",n,"th character is",value,end = '')