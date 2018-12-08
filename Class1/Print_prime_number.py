num = int(input("Type a number >5: "))

for i in range(2,num-1):
    if(num%i == 0):
        print("Number is not prime")
        break