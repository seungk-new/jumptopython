#함수 안에서 함수 밖의 변수를 변경하는 방법
#return, global, lambd사용하기.
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)
a = 1
def vartest():
    global a #global은 안 쓰는 게 좋음, 외부 변수에 종속적인 함수는 그다지 좋은 게 아님.
    a= a + 4
vartest()
print(a)

#lambda는 def와 동일한 역할, 함수를 한줄로 간결하게 만들 때, def못쓸 때 사용.
#lambda 매개변수1, 매개변수2,... : 매개변수를 이용한 표현식
add = lambda a, b : a + b
result = add(3, 4)
print(result)
#add는 두개의 인수를 받아 서로 더한 값을 돌려주는lambda함수이다.
def add(a, b):
    return a + b
result = add(44, 4)
print(result)
#lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.