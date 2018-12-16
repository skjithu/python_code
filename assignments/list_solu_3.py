import sys
mylist = [5,39,24,50,1,75,26]

max = -sys.maxsize - 1

#max = -1000000
for item in mylist:
    if item>max:
        max = item
print(max)