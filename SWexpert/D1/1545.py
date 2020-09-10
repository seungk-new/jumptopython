import sys
sys.stdin = open("1545_input.txt", "r")
T = int(input())
for i in range(8, -1 ,-1):
    print(i, end = ' ')