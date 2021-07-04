# #클래스를 무작정 만들기 보다는 클래스로 만든 객체를 중심으로
# #어떤 식으로 동작하게 할 것인지 미리 구상한 후 생각한 것들을 하나씩 해결.

# #사칙연산을 가능하게 하는 Fourcal클래스
# class Fourcal:
#     pass #pass를 포함한 Fourcal클래스 생성, 현재 상태에서 Fourcal클래스는 아무
# #변수나 함수도 포함하지 않지만 우리가 원하는 객체 a를 만들 수 있는 기능은 가지고 있다.
# a = Fourcal()
# print(type(a))#a가 Fourcal클래스의 객체임을 알 수 있다.
# #객체에 숫자 지정할 수 있게 만들기
# #이제 사칙연산 기능을 가진 객체들을 만들어야 한다. 그런데 일단
# #사칙연산을 하려면 a객체에 사칙연산을 할 때 사용할 2개의 숫자를 알려줘야함.
# a.setdata(4, 2)
# class Fourcal:
#     def setdata(self, first, second):
#         self.first = first #매서드의 수행문 두 개
#         self.second = second #앞에서 만든 Fourcal클래스에 pass를 지우고
    #setdata함수를 만들었다. 클래스 안에 구현된 함수를 메서드(Method)
#라고 부른다. 앞으로 클래스 내부의 함수는 항상 매서드라고 표현하자.
# a = Fourcal()
# a.setdata(4, 2)
# print(a.first)
# print(a.second)

# a = Fourcal()
# b = Fourcal()
# a.setdata(4, 2)
# print(a.first)
# print(a.second)
# b.setdata(3, 7)
# print(b.first)
# print(b.second) #클래스로 만든 객체변수는 다른 객체의 객체변수에 상관없이 독립적인
# #값을 유지한다.
class Fourcal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# b = Fourcal()
# a.setdata(4, 2)
# b.setdata(3, 8)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

#클래스를 상속하기 위해서는 클래스 이름 괄호 뒤에 상속할 클래스의 이름을 넣어주면 된다.
# class MoreFourcal(Fourcal):
    # pass
# a = MoreFourcal(4, 2)
# print(a.add())

class MoreFourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourcal(4, 2)
print(a.pow())

#매서드 오버라이딩
# a = Fourcal(4, 0)
# print(a.div())
#위와 같이 하면 zero division 오류가 뜸, 대신 0을 돌려주고 싶다면?
class Safefourcal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = Safefourcal(4, 0)
print(a.div())
#Safefourcal클래스는 Fourcal클래스에 있는 div 매서드를 동일한 이름으로 다시 작성,
#부모 클래스(상속한 클래스)에 있는 매서드를 동일한 이름으로 다시 만드는 것을
#매서드 오버라이딩(overriding, 덮어쓰기)라고 한다.
#이렇게 매서드를 오버라이딩 하면 부모클래스 대신 오버라이딩한 매서드가 호출된다.
