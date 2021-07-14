emptyone = []
emptytwo = []

for i in range(19):
    emptyone.append([])
    for j in range(19):
        emptyone[i].append(0)
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    emptyone[x -1][y - 1] = 1

for i in range(19):
    for j in emptyone[i]:
        print(j, end = ' ')
    print()



