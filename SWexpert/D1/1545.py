import sys
sys.stdin = open("1545_input.txt", "r")
number = int(input())
for i in range(number,-1,-1):
    print(i, end=' ')