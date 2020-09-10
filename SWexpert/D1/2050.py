import sys
sys.stdin = open("2050_input.txt", "r")
string = input()
for char in string:
    print(ord(char)-64, end= ' ')
