frequency = {}

def calculatefrequency(line):
    global frequency
    word_list = line.split(",")
    print(word_list)
    for word in word_list:
        tmp = word.strip()
        print(tmp)
        if tmp in frequency:
            val = frequency[tmp]
            val = val+1
        else:
            frequency[tmp] = 1

with open("sample.txt", "r") as myfile:
    line = myfile.readline()
    while(line):
        calculatefrequency(line)
        line = myfile.readline()

print(frequency)