import sys
sys.stdin = open("2072_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    datas = list(map(int, input().split()))
    print(f'#{test_case}{int(round(sum(datas)/10, 0))}')  
  