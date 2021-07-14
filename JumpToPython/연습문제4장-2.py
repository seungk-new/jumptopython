#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
#(단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# 평균 값을 구할 때는 len함수를 사용해 보자.

##입력으로 몇 개가 들어올지 모르니까 *args사용
def pg(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)
print(pg(1, 2, 3, 4, 5))