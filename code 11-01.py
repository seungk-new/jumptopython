## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

## 변수
# testAry = [55, 88, 33, 77]
import random ## 테스트용
before = [random.randint(100, 999) for _ in range(20)] ## 테스트용
after = []
## 메인코드
print('정렬 전-->', before)
for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos]) ## 정렬하기 전의 방에 있던 값을 지워주는 

print('정렬 후-->', after)

# print(testAry)
# minPos = findMinIndex(testAry)
# print('최솟값-->', testAry[minPos])