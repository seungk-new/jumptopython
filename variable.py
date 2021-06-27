a = 1 # =은 assignment라고 한다.
b = 'python'
c= [1, 2, 3]
#  C나 JAVA에서는 변수를 만들 때 자료형을 직접 지정해야 하지만 파이썬은
# 변수에 저장된 값을 스스로 판단하여 자료형을 저장한다.
#변수이름 = 변수에 저장할 값 이런 형태.
#변수는 객체를 말한다. 객체는 지금까지 한 자료형 같은 것을 의미.
# a = [1, 2, 3]의 경우 [1, 2, 3]값을 가지는 리스트 자료형(객체)이 자동으로 
#메모리에 생성되고 변수 a는 [1, 2, 3]리스트가 저장된 메모리의 주소를 가리키게 됨.
a = [1, 2, 3]
print(id(a)) #이처럼 id(변수이름)을 통해 변수가 가리키는 메모리 주소 파악 가능.
a = [1, 2, 3]
b = a #[1, 2, 3]리스트를 참조하는 변수가  기존에 a 하나에서 b까지 두 개로 늘어남.
#b는 a와 완전히 동일하다 할 수 있음.
print(a is b) #이를 통해 a와 b가 완전히 동일하다는 것 확인가능.
a[1] = 4
print(a)
print(b)
#그렇다면, b변수를 생성할 때 a변수의 값은 가져오되 a와는 다른 주소를 갖게 하려면?
#두가지 방법 중 첫번째 [:]이용하기 [:]는 리스트 전체를 가리킴.
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)
#두번째 방법으로 copy모듈 이용하기
from copy import copy #파이썬 모듈부분에서 자세히 다룰 예정.
a = [1, 2, 3]
b =copy(a)
print(b is a)
#리스트 자료형의 자체함수인copy함수를 사용해도 copy모듈을 사용하는 것과 동일함.
a = [1, 2, 3]
b = a.copy()
print(b is a)
a, b = ('python' , 'life')
(a, b) = 'python', 'life'#튜플은 괄호를 생략해도 된다고 했음.
[a, b] = ['python', 'life'] #리스트도 변수로 만들 수 있음.
a = b ='python' #이처럼 여러개의 변수에 하나의 값을 저장할 수도 있음.
a = 3
b = 5
a, b = b, a
print(a)
print(b)
