## 함수
def add_data(friend): # 함수 = Function = 기능
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None
    katok[position] = friend

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position + 1, kLen, 1):
        katok[i - 1] = katok[i]
        katok[i] = None
    del(katok[kLen - 1])


## 전역
katok = []
select = -1 # 1추가, 2삽입, 3삭제, 4종료

## 메인
while (select != 4):
    select = int(input('선택(1추가, 2삽입, 3삭제, 4종료)-->'))

    if(select == 1):
        data = input('추가할 친구-->') # 추가작동
        add_data(data)
        print(katok)
    elif(select == 2):
        pos = int(input('삽입할 위치-->'))
        data = input('삽입할 친구-->') # 삽입작동
        insert_data(pos, data)
    elif(select == 3):
        pos = int(input('삭제할 위치-->'))# 삭제작동
        delete_data(pos)
        print(katok)
    elif(select == 4):
        print(katok) # 종료작동
    else:
        print("잘못입력하였습니다.")