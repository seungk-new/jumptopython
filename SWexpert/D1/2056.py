import sys
sys.stdin = open("2056_input.txt", "r")
ref = [0, 31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30 , 31 ]
T = int(input())
for test_case in range(1, T + 1):
    data = input()
    year = data[0:4]
    month = data[4:6]
    day = data[6:8]
    
    if ref[int(month)] >= int(day):
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} -1')
        
        
            
