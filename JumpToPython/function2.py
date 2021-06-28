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

result = add_mul("mul", 1, 2, 3, 5)
print(result)