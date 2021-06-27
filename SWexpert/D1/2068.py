import sys
sys.stdin = open("2072_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    datas = list(map(int, input().split()))
    result = datas[0]
    for i in range(len(datas)):
        if result < datas[i]:
            result = datas[i]
       print(result)

