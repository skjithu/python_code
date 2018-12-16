num1 = int(input("Enter the lower range: "))
num2 = int(input("Enter the upper range: "))

for i in range (num1,num2+1):
    if (i%7 == 0) and (i%5 == 0):
        print(i)