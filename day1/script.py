
input = open("day1/input.txt","r")

elfCarryWeight = []

elfCalories = 0
for element in input:
    if element == "\n":
        elfCarryWeight.append(elfCalories)
        elfCalories = 0
    else:
        elfCalories += int(element)

print("max snakcs :",max(elfCarryWeight))

elfCarryWeight.sort(reverse=True)

print("calories of top3 :",sum(elfCarryWeight[0:3]))