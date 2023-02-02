dict = {}
ans = 'y'
anss = 'y'

while ans == 'y':
    product, prices = eval(input("Enter product, prices: "))
    dict[product] = prices

    ans = input("More products?(y/n)")

print(dict)

while anss == 'y':
    name = input("Enter the product name: ")
    if name in dict:
        print("Product found! ")

    else:
        print("Product not found! ")

    anss = input("More products?(y/n)")