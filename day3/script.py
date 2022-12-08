from difflib import SequenceMatcher
input = open("day3/input")
sum = 0
convert = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 1
for letter in alphabet:
    convert[letter] = i
    i += 1
for letter in alphabet.upper():
    convert[letter] = i
    i += 1
sum = 0
for backpackContent in input:
    size = len(backpackContent)
    left = backpackContent[0:size//2]
    right = backpackContent[size//2:]
    match = SequenceMatcher(None, left,right).find_longest_match()
    sum += convert[left[match.a:match.a+match.size]]
print (sum)
input = open("day3/input")
fullText = input.read()
bags = fullText.split("\n")
sum2 = 0
found = False
for i in range(len(bags)//3):
    elf1 = bags[3*i]
    elf2 = bags[3*i+1]
    elf3 = bags[3*i+2]
    found = False
    for letter1 in elf1:
        for  letter2 in elf2:
            if (letter1 == letter2):
                for letter3 in elf3:
                    if(letter3 == letter1 and not found):
                        sum2 += convert[letter3]
                        found = True
print(sum2)