#import collections

mylist = [1,1,1,2,2,2,2,3,3,4,4,4,5,5,5,5,5,5,5,5,6,6,6,7,7,8,8,8,9,9,10,10,10,10,10]

#num = int(input("Tell me a number: "))

frequency = {}

for num in mylist:
    if num in frequency:
        val = frequency[num]
        val = val+1
        frequency[num] = val
    else:
        frequency[num] = 1

print(frequency)

#outputstring = "Tell me a number: "

#num = int(input(outputstring))

#print(frequency)