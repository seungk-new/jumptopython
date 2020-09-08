import sys
sys.stdin = open("2019_input.txt", "r")
#2*2*2*2*2*2*2*2
#2를 T개 만큼 곱하게 한다.
T = int(input())
#i = 0 
for i in range(0, T+1):
    #i += 1
    if T < 30:
        print(2 ** i, end =' ')
        
    
