import sys
sys.stdin = open("1986_input.txt", "r")
T=int(input())
for test_case in range(1, T + 1):
    data = int(input())
    sum = 0
    for i in range(1, data+1):
        if i % 2 == 0:
            sum -=i
        else:
            sum += i
    print(f'#{test_case} {sum}')

    

        
