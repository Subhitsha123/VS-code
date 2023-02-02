seq_a = eval(input("Enter tuple a: "))
seq_b = eval(input("Enter tuple b: "))
count = 0

for i in range(len(seq_a)):
    if seq_a[i] in seq_b:
        count+=1

if count == len(seq_a):
    print("True")

else:
    print("False")