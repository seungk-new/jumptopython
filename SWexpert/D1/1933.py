import sys
sys.stdin = open("1933_input.txt", "r")
data = int(input())
for i in range(1, data + 1):
    if data % i == 0:
        print(i, end = ' ')
