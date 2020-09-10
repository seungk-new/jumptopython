import sys
sys.stdin = open("2043_input.txt", "r")
P, K = list(map(int, input().split()))
print(P - K + 1)

