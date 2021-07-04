#bool은 오직 True와 False 두 가지 값만 가진다.
#True, False 첫 글자는 항상 대문자.
a = True
b = False
print(type(a))
print(type(b)) # type함수를 통해 ()안의 자료형 파악 가능.

#bool자료형은 조건문의 반환값으로도 사용 가능
print(1 == 1)

'''자료형에는 참과 거짓이 있다.
참인것-> 'python', 1, [1,2,3]처럼 
문자열, 리스트, 튜플, 딕셔너리 등의 값이 채워져 있으면 참임.
거짓인것-> "",[],(),{},0,None'''

a = [1, 2, 3, 4]
while a: #while문은 조건이 참인 동안만 실행된다.
    print(a.pop())
'''a.pop함수는 리스트의 마지막 값을 끌어내는 함수로
마지막 요소인 4를 끌어내고 
그 다음에 남은 것중 마지막 요소인 3을 끌어내고 쭈욱 반복
다 끌어내서 빈리스트가 되면 []는 거짓이니까 while문이 끝남'''
if[]:
    print('참')
else:
    print('거짓') 
#이 경우도 마찬가지로 []는 거짓이니까 else의 수행문인 거짓 반환
if [1, 2, 3]:
    print('참')
else:
    print('거짓')
    #[1, 2, 3]이 참이니까 if조건문의 실행문인 참 반환.

print(bool('python')) #'python'은 빈 문자열이 이니라서 True 반환.
print(bool('')) # ''은 빈 문자열이라 False반환.

print(bool(3))
print(bool([]))