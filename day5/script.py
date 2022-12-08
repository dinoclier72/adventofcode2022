input = open("day5/input")
str = input.read()
lst = str.split('\n')
stacks = []
i = 0
while(lst[i] != ''):
    i += 1
numbers = lst[i-1].split(' ')
j = len(numbers)-1
while(numbers[j] == ''):
    j -= 1
towersnumber = int(numbers[j])
for j in range(towersnumber):
    stacks.append([])
for j in range(i-2,-1,-1):
    for k in range(towersnumber):
        crate = lst[j][k*4:k*4+3]
        if(crate != '   '):
            stacks[k].append(crate)
for j in range(i+1,len(lst)-1):
    instruction = lst[j].split(' ')
    quantity = int(instruction[1])
    boxFrom = int(instruction[3])-1
    boxto = int(instruction[5])-1
    selection = stacks[boxFrom][len(stacks[boxFrom])-quantity:len(stacks[boxFrom])]
    for element in selection: #ajouter [::-1] pour inverser la selection simule le picking un par un
        stacks[boxto].append(element)
    del(stacks[boxFrom][len(stacks[boxFrom])-quantity:len(stacks[boxFrom])])
str = ""
for j in range(len(stacks)):
    str += stacks[j][len(stacks[j])-1][1]
print(str)
#version 1 JDTMRWCQJ