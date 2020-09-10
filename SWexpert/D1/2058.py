import sys
sys.stdin = open("2058_input.txt", "r")
T = list(map(int, input()))
result = 0
for number in T:
    result += number
print(result)

#print(sum(T))

# data = input()
# result = 0 
# for i in data:
#     result += int(i)
# print(result)

