import sys
sys.stdin = open("2063_input.txt", "r")
T=int(input())
data = list(map(int, input().split()))
center = len(data)//2
data.sort()
print(data[center])
