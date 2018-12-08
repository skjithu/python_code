data = input("Please enter a string: ")

count = 0
for char in data:
    if char in "aeiouAEIOU":
        count = count + 1

print("There are {} vowels in the given sentence". format(count))
