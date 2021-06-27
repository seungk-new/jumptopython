import sys
sys.stdin = open("2047_input.txt", "r")
#string = input()
# 문자에서 숫자로 ord
# 숫자에서 문자로 chr
#소문자 인풋을 ord로 받아서 숫자로 변환->인풋 내 소문자 하나에
#대응되는 대문자 ord 빼주고 해당 차이만큼 소문자 인풋 ord에 더해줌
# 그다음 chr을 이용해 숫자를 대문자로 변환
 #소문자가 대문자 보다 32크다.
# 1. T리스트의 각 요소값을 숫자로 변환해 준다.
# 2. 변환된 숫자에 32씩 더해 준다.
# 3. 더한 값을 프린트한다.

#print(ord('a') - ord('A'))
"""result = ''
for char in string:
    if(ord('a') <= ord(char) <= ord('z')):
        result += chr(ord(char) - (ord('a') - ord('A')))
    else:
        result += char
print(result)"""

"""string = input()
result = ''
for char in string:
    if(ord('A') <= ord('Z')):
        result += char
    elif (ord('a') <= ord('z')):
        result += chr(ord(char)) - (ord('a') - ord('A'))
    elif():
        result += char
print(result)"""


string = input()
result = ''
for char in string:
    if (ord('a') <= ord(char) <= ord('z')):
        result += chr(ord(char) - (ord('a') - ord('A')))
    else:
        result += char      
print(result)