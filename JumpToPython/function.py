def add(a, b):
    return  a + b
    #이 함수의 이름은 add이고 입력으로 2개의 값을 받으며
    #결괏값은 2개의 입력값을 더한 값이다 라는 뜻.
a = 3
b = 4
c = add(a, b)
print(c)
#매개변수(prarameter)는 입력을 받는 값
#인수(arguments)는 입력이 되는 값

#def 함수이름(매개변수):
    #<수행할 문장>
    #return 결괏값

#입력값이 없는 함수
def say():
    return 'HI'
a = say() #결괏값을 받을 변수 = 함수이름()
print(a) #a에 'HI'문자열이 대입되는 것.

#결괏값이 없는 함수
def add(a, b):
    print("%d과 %d의 합은 %d입니다." %(a, b, a+ b))
add(3, 4)
#결괏값이 없는 함수는 함수이름(입력인수1, 입력인수2, ...)처럼 사용.
def say():
    return 'HI'
a = say()
print(a)

def say():
    print('hi')
say()

#매개변수 지정하여 호출하기
def add(a, b):
    return a + b
result = add(a = 3, b = 7)
print(result)