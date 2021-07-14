# for 변수 in 리스트(또는 튜플, 문자열):
    #수행할 문장1 이런 식으로 진행됨.
test_list = ['one', 'two', 'three'] #test_list안에 있는 게 하나하나 변수임.
for i in test_list:
    print(i)

#다양한 for문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
#위의 for문에서 리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로
#(first, last)변수에 대입된다.
#(first, last) = (1, 2)이런 식으로 튜플을 사용한 변수값
#대입 방법과 매우 비슷한 경우

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면
#불합격이다. 합격인지 불합격인지 결과 보여주자.
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('%d번 학생은 합격입니다.' %number)
    else:
        print('%d번 학생은 불합격입니다.' %number)

#위와 같은 경우인데 continue문을 사용해서 for문의 처음으로 돌아가게 할 수도 있다.
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print('%d번 학생 축하합니다. 합격입니다' %number)

#for문과 함께 자주 사용하는 range 함수
#for문은 숫자 리스트를 자동으로 만들어 주는 range함수와 함께 사용하는 경우가
#많다. 다음은 range함수의 간단한 사용법이다.
a = range(10)
print(a)#range(10)은 0부터 10미만의 숫자를 포함하는 range 객체를 만들어 준다.
#시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자)형태를 사용하는데,
#이 때 끝 숫자는 포함하지 않는다.
a = range(1, 11)
print(a)
#range함수의 예시
add = 0
for i in range(1, 11):
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격이니다." %(number+1))

#for와 range를 이용한 구구단
#for와 range 함수를 사용하면 소스코드 단 4줄만으로 구구달을 출력할 수 있다.
#들여쓰기에 주의하며 입력해보자.
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print("")
    # end = ""를 써주는 이유는 해당 결괏값을 출력할 때 다음줄로
    #넘기지 않고 그 줄에 계속해서 출력하기 위해서임.
    #print("")을 마지막에 써 준 이유는 2단, 3단 등을 구분하기 위해 두 번째
    #for문이 끝나면 결괏값을 다음 줄부터 출력하게 해주는 문장임.

#리스트 내포 사용하기
#리스트 안에 for문을 포함하는 리스트 내포(List comprehension)를 사용하면 좀 더
#편리하고 직관적인 프로그램을 만들 수 있다.
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)
#위의 예제는 a리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담는 예제임.
#이것을 리스트 내포를 사용하면 다음과 같이 간단히 해결 가능
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)
#만약 짝수에만 3을 곱한 거 반환하고 싶으면
result = [num * 3 for num in a if num % 2 == 0]
print(result)
#만약 구구단의 모든 결과를 리스트에 담고 싶다면 리스트 내포를 사용하여 다음과 같이 간단하게 구현할 수도 있다.
result = [a * b for a in range(2, 10)
for b in range(1, 10)]
print(result)

    
