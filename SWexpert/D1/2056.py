import sys
sys.stdin = open("2056_input.txt", "r")
ref = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, 
'07':31, '08':31,'09':30, '10':31, '11':30 , '12':31 }

T = int(input())
for test_case in range(1, T + 1):
    data = input()
    year = data[0:4]
    month = data[4:6]
    day = data[6:8]
    
    if ref.get(month, -1) >= int(day):
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} -1')
        
        
            
