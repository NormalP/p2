l = list(map(int,input().split()))
num = 0
for i in range(int(len(l) / 2)):
    l[num], l[num+ 1] = l[num + 1], l[num]
    num += 2

print(l)