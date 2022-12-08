input = open('day4/input')
count = 0
overlap = 0
for line in input:
    group = line.rstrip().split(',')
    elfrooms = []
    for rooms in group:
        roomsRange = []
        rooms = rooms.split("-")
        roomsRange.append(int(rooms[0]))
        roomsRange.append(int(rooms[1]))
        elfrooms.append(roomsRange)
    if(elfrooms[0][0]<=elfrooms[1][0] and elfrooms[0][1] >= elfrooms[1][1] or elfrooms[1][0]<=elfrooms[0][0] and elfrooms[1][1] >= elfrooms[0][1]):
        count += 1
    if(elfrooms[0][0] in range(elfrooms[1][0],elfrooms[1][1]+1) or elfrooms[0][1] in range(elfrooms[1][0],elfrooms[1][1]+1) or elfrooms[1][0] in range(elfrooms[0][0],elfrooms[0][1]+1) or elfrooms[1][1] in range(elfrooms[0][0],elfrooms[0][1]+1)):
        overlap += 1
print(count)
print(overlap)