#while조건문은 조건문이 참인 경우 동안 계속 실행된다.
treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다" %treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")
# treehit이 10보다 작을 동안은 계속해서 while문이 돌아가고
#treehit이 10이 되면 나무넘어갑니다 프린트함.
print(type(treehit))

#while문 만들기
prompt = """
1. add
2. Del
3. List
4. quit

Enter number : """
#이어서 number변수에 0을 먼저 대입한다. 이렇게 변수를 설정해 놓지 않으면
#다음에 나올 while문의 조건문인 number !=4에서 변수가 존재하지 않는다는
#오류가 발생한다.
number = 0
while number != 4:
    print(prompt)
    number = int(input()) #터미널에 4를 직접 입력하기 전까지는 계속해서 prompt를 출력한다.
    #4를 입력하면 조건문이 거짓이 되어 while문을 빠져나가게 된다.
#while문에서 강제로 빠져나가기 위해서는 break문을 사용해야 한다.
# 커피 자판기에 커피가 없어서 판매종료 되는 경우.
coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee - 1
    print('남은 커피의 양은 %d입니다' %coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break
#while문의 맨 처음으로 돌아가기
#1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while문을 사용해서 작성한다고
#생각해보자. 어떤 방법이 좋을까?
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:continue
    print(a)
    #a가 10보다 작은 동안 a는 1만큼씩 계속 증가한다. 

