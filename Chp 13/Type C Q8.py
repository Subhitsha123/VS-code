x = {'k1':'v1', 'k2':'v2', 'k3':'v3'}

inverted_dict = {}

for key in x:
    inverted_dict[x[key]] = key

print(inverted_dict)