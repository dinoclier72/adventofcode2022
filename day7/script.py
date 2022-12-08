input = open("day7/input.txt")
cmd = input.read().split("\n")
# def listallfiles(str):
#     files = dict()
#     for e in str:
#         if(e[0] == "$"):
#             if(e[2:4] == "cd"):
#                 var = e[4:]
#             if(e[2:4] == "ls"):
#                 files[var] = dict()
#         else:
#             infos = e.split(" ")
#             if(infos[0] == "dir"):
#                 files[var][infos[1]] = dict
#             else:
#                 files[var][infos[1]] = infos[0]
#     return files
#print(listallfiles(cmd))
def advancedLAF(Lstr):
    files = {"/" : dict()}
    back = []
    back.append((files["/"],"/"))
    file = files
    for str in Lstr:
        str = str.rstrip()
        if(str[0] == "$"):
            if(str[2:4] == "cd"):
                var = str[5:]
                for i in range(len(back)):
                    if(var == back[i][1]):
                        file = back[i][0]
        else:
            infos = str.split(" ")
            if(infos[0] == "dir"):
                file[infos[1]] = dict()
                back.append((file[infos[1]],infos[1]))
            else:
                file[infos[1]] = infos[0]
    return files
files = advancedLAF(cmd)
def sumofsize(dict):
    sum = 0
    for key,item in dict.items():
        if(type(item) == type(dict)):
            sum += sumofsize(dict[key])
        else:
            sum += int(item)
    if(sum > 100000):
        return 0
    return sum
print(sumofsize(files))