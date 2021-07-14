#클래스 변수
#객체변수는 다른 객체들에 영향을 받지 않고 독립적으로 그 값을 유지한다는 것,
#이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아보자.
class Family:
    lastname = "김"
#Family 클래스에 선언한 lastname이 클래스 변수이다. 클래스 변수는 클래스 안에 함수를
#선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.

print(Family.lastname)
#클래스 변수는 위 예와 같이 (클래스이름, 클래스변수)로 사용가능
#또는 다음과 같이 Family클래스로 만든 객체를 통해서도 클래스 변수를 사용가능.
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
#만약 Family클래스의 lastname을 다음과 같이 '박'이라는 문자열로 바꾸면?
Family.lastname = '박'
print(a.lastname)
print(b.lastname)
#클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname값도 모두 변경됨
#즉, 클래스 변수는 클래스로 만든 모든 객체에 공유됨.