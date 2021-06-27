import sys
sys.stdin = open("2025_input.txt", "r")
data = int(input())
result = 0
for data in range(1, data+1):
    result += data
print(result)