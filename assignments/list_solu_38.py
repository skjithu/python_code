#change the position of every n-th value with the (n+1)th in a list

mylist = [0,1,2,3,4,5]

for i in range(0,len(mylist)-1):
    mylist[i],mylist[i+1] = mylist[i+1],mylist[i]

print(mylist)