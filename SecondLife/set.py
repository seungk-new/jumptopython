s1 = set([1, 2, 3]) #집합자료형을 만든다 set키워드를 이용해서.
print(s1)
#위와 같이 set()안에 리스트를 입력하여 만들 수도 있고 아래와 같이 문자열을 입력할 수도 있음.
s2 = set('hello')
print(s2) 
#비어 있는 집합 자료형은 s = set()로 만들 수 있다.

#set은 중복을 허용하지 않고 순서가 없다(unordered)
#순서가 있다면 인덱싱을 통해 값을 얻을 수 있지만 set은 순서가 없어서 인덱싱으로 값을 얻을 수 없다.
#딕셔너리가 순서가 없어서 인덱싱을 사용하지 못하는 것처럼..

#따라서 set자료형에 저장된 값을 인덱싱으로 얻고 싶으면 리스트나 튜플로 변환을 먼저 해야함!
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
t1 = list(s1)
print(s1)
print(t1[0])

#set자료형을 사용해서 교집합, 합집합, 차집합을 구할 수 있다.
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1.intersection(s2)) # &기호 혹은 intersection함수는 교집합
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))#합집합도 |기호나 union 함수로 가능.

print(s1 - s2)
print(s2 - s1)# -를 사용하거나 difference를 사용해서도 차집합 구하기 가능.

#s1.add같이 add를 써서 값을 한 개 추가 할 수도 있다.
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#s1.update를 통해서는 값을 여러개 추가 할 수 있다.
s1.update([4, 4, 5, 6])
print(s1)

#s1.remove를 통해 값을 제거 할 수도 있다.
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)



