input = open("day6/input")
def detectStart(str,length):
    for i in range(len(str)-length):
        pack = []
        for j in range(length):
            pack.append(str[i+j])
        if(len(pack) == len(set(pack))):
            return i+length
str = input.read()
startconv = detectStart(str,14)
print(startconv)