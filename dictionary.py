#key값에는 변하지 않는 값을 사용하고 value값에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.
#value에 list도 넣을 수 있다.

#딕셔너리에 쌍 추가하기
a = {1 : 'a'}
a[2] = 'b' #2라는 키값에 b라는 value값을 넣어줌.
print(a)
a['name'] = 'pey' #name이라는 키값에 pey라는 벨류값을 넣어줌.
print(a)
a[3] = [1, 2, 3] #3이라는 키값에 리스트를 벨류로 넣어줌.
print(a)
#딕셔너리 사용의 예시-> {'김연아' : '피겨', '류현진' = '야구'}처럼 사람과 특징 매칭에 사용 가능.

#key값을 이용해서 value를 얻어보자
grade = {'pey' : 10, 'julliet' : 90}
print(grade['pey'])
grade['pey'] = 20
print(grade['pey']) #벨류값을 변형 해줘봄.
#리스트나 튜플은 요솟값을 얻고 싶으면 인덱싱이나 슬라이싱 하지만
#딕셔너리는 key를 통해 value를 구하는 방법뿐!
a = {1 : 'a', 2 : 'b'}
print(a[1])
dic = {'name' : 'pey', 'phone' : '011999', 'birth' : '118'}
print(dic['name'])

#딕셔너리에서 key값은 고유한 값이므로 중복되는 key값을 설정해 놓으면 하나를 제외한 나머지는 무시됨.
a = {1:'a', 1 : 'b'}
print(a[1])
#딕셔너리에서 key값은 변할 수 없기 때문에 key값으로 리스트를 쓰지 못한다. 대신에 튜플은 변할 수 있어서 key값으로 사용가능.

#딕셔너리가 자체적으로 가지고 있는 함수
a = {'name' : 'pey', 'phone' : '123213213', 'birth' : '1212'}
print(a.keys()) #a.keys()는 딕셔너리 a의 key값만을 모아서 dict_keys 객체를 돌려준다.
#파이썬 3.0이후로 반환값으로 list를 받고 싶으면 list(a.keys())해주면 됨.
for k in a.keys():  #dict_keys객체를 사용하는 방법
    print(k)
#value 리스트 만들기
print(a.values())
#key : value 쌍으로 모두 지우기
a.clear()
print(a) #빈 리스트를 [], 빈 튜플을 ()로 표현하는 것처럼 빈 딕셔너리도 {}로 표현.
#key로 value얻기
a = {'name' : 'pey', 'phone' : '123123', 'birth' : '1212'}
print(a.get('name'))
print(a.get('phone')) #get(x)라는 함수는 x라는 key에 대응되는 value를 돌려준다.
print(a['name']) #a.get('name')을 사용하는 것과 a['name']을 사용하는 것은 동일한 결과.
#다만, a.get(x)라는 함수를 사용하면 x라는 키가 존재하지 않을 때 None을 돌려주고 a['x']는 오류가 난다.

print(a.get('foo', 'bar')) #이것은 foo라는 키값이 a에 없는데 bar를 돌려주고 싶을 때 쓴다.

# 해당 key가 딕셔너리 안에 있는지 어떻게 알까?
a = {'name' : 'pey', 'phone' : '1231232', 'birth' : '1212'}
print('name' in a) # 'name'이라는 key가 a라는 딕셔너리에 있는지 확인해서 truesk false로 돌려줌.

