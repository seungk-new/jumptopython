test_case = int(input())

board = []
white = []
temp = []

for _ in range(1, test_case+1):
    a,b = map(int, (input().split()))
    white.append([a,b])

white.sort()

for _ in range(1,6):
    temp.append(0)
    board.append(temp)

# for i in white:
#     print(i)
#     board[i[0]-1][i[1]-1] = 1
board[0][0]=1
print(board[0])
print("--")
print(board[0][1])
print("--")
print(board)
    

    