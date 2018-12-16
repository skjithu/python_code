# remove duplicates from the list

mylist = [1,1,1,2,2,3,4,0,5,5,6,7,3,4,8,9,6,9,8,0]

mydict = {}
for item in mylist:
    mydict[item] = "Random staff"
res = list(mydict.keys())
print(res)