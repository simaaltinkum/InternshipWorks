import sum
import subtraction

num = int(input("How many operations will you do?: "))
for i in range (0,num):
    operation = int(input("Select 1 for sum, select 2 for subtracting: "))
    if operation == 1:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(sum.add(a,b))
    elif operation == 2:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(subtraction.sub(a,b))
