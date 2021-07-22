## 함수
def binSearch(ary, fData): #바이너리 서치 == 이진탐색
    pos = -1
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start+end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos
## 전역변수
dataAry = [23, 33, 44, 55, 66, 77, 88, 99, 100, 101]
findData = 88 # 할머니키
## 메인코드
print('배열-->', dataAry)
position = binSearch(dataAry, findData)
if position == -1:
    print('없음')
else:
    print(findData, '는 ', position, '위치에 있음')