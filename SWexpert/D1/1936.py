import sys
sys.stdin = open("1936_input.txt", "r")
A, B = map(int, input().split())
if A > B:
    print('A')
else:
    print('B')
