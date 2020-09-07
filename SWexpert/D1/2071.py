import sys
sys.stdin = open("2072_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    datas = list(map(int, input().split()))
    sum = 0
    for data in datas:
        sum += data
    print(f'#{test_case} {sum/10}')