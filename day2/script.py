input = open("day2/input")

score = 0
for match in input:
    joue = match.rstrip().split(' ')
    if(joue[1] == "X"):
        score += 1
        if(joue[0] == "A"):
            score += 3
        if(joue[0] == "C"):
            score += 6
    if(joue[1] == "Y"):
        score += 2
        if(joue[0] == "B"):
            score += 3
        if(joue[0] == "A"):
            score += 6
    if(joue[1] == "Z"):
        score +=3
        if(joue[0] == "C"):
            score += 3
        if(joue[0] == "B"):
            score += 6

print("part 1: score total",score)

input = open("day2/input")
score = 0
for match in input:
    joue = match.rstrip().split(" ")
    if(joue[0] == "A"):
        if(joue[1] == "X"):
            score += 3
        if(joue[1] == "Y"):
            score += 4
        if(joue[1] == "Z"):
            score += 8
    if(joue[0] == "B"):
        if(joue[1] == "X"):
            score += 1
        if(joue[1] == "Y"):
            score += 5
        if(joue[1] == "Z"):
            score += 9
    if(joue[0] == "C"):
        if(joue[1] == "X"):
            score += 2
        if(joue[1] == "Y"):
            score += 6
        if(joue[1] == "Z"):
            score += 7

print("part 2 score:",score)