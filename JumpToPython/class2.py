# 클래스를 사용하기.
# class Calculator: #Calculator라는 클래스는 일종의 과자 틀
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result
#     def sub(self, num):
#         self.result -= num
#         return self.result

# cal1 = Calculator()#cal1,2,3 이런 것은 과자틀에 의해 만들어진 과자(객체라고 함)
# cal2 = Calculator()
# cal3 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
# print(cal3.sub(3))
# print(cal3.sub(2))

class Cookie: #아무 기능도 갖고 있지 않은 껍질뿐인 클래스임.
    pass
a = Cookie() #Cookie()의 결괏값을 돌려받은 a와 b가 객체임.
b = Cookie()
#클래스로 만든 객체를 인스턴스라고도 한다.
#그렇다면 객체와 인스턴스의 차이는 무엇일까?
#a = Cookie()라는 게 있을 때 a만 그냥 말할 때 a는 객체라고 하고
#Cookie클래스와의 관계로 말할 때 인스턴스(instance)라고 한다.
# 즉 어떤 클래스의 객체인지 관계 위주로 설명할 때 인스턴스라고 한다.
# a는 Cookie의 객체라고 하기보다는 a는 Cookie의 인스턴스라는 표현이 좋음.
