#입력값이 몇 개가 될지 모를 때는 어떡할까?
#def 함수이름(*매개변수)
#<수행할 문장>
#여러 개의 입력값을 받는 함수 만들기
#add_many(1, 2)이면 3을 add_many(1, 2, 3)이면 6을 반영하는 함수 만들기

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
#위에서 만든 add_mamy함수는 입력값이 몇 개이든 상관없음.
# *을 매개변수 이름 앞에 붙여주면 입력값을 전부 모아서 튜플로 만들어주기 때문이다.
result = add_many(1, 2, 3)
print(result)
result = add_many(2,3, 4, 5, 5)
print(result)
#여러 개의 입력을 처리할 때  def add_many(*args)처럼 함수의 매개변수로 *args만 사용할 수 있는 것은 아니다.

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result
result = add_mul("add", 1, 2, 3)
print(result)

result = add_mul("mul", 1, 2, 3)
print()
#키워드 파라미터 kwargs, 키워드 파라미터를 사용할 때는 매개변수 앞에 **를 붙인다.
def kwargs(**kwargs):
    print(kwargs)
kwargs(a=1)
kwargs(name = "foo", age=3)
#**kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수
#kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.

#함수의 결괏값은 언제나 하나이다.
def add_and_mul(a, b):
    return a+b, a*b
result = add_and_mul(2, 3)
print(result)
#함수의 결괏값은 언제나 하나이다.(a+b, a*b)튜플 형식으로 돌려준다.
#매개변수에 초깃값 미리 설정하기
# return의 또 다른 쓰임새
#특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를
#즉시 빠져나갈 수 있다.

def rainbow(color):
    if color == "연두색":
        return
    print("무지개에 있는 색은 %s입니다" %color)
rainbow('검정색')
rainbow("연두색")#이 때는 빠져나가짐.
rainbow("빨간색")

#매개변수에 초깃값 미리 설정하기.
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
say_myself("vic", 29)
# 초기화 시키고 싶은 변수를 항상 맨 뒤에 놓아야함.man = True와 같은 것.
