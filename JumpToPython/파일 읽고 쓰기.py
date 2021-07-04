# # # f = open("C:/Users/tmdrb/새파일.txt", 'w')
# # # for i in range(1, 11):
# # #     data = "%d번째 줄입니다.\n"%i
# # #     f.write(data)
# # # # f.close()

# # # #프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
# # # #readline(), readlines, read이용
# # # f = open("C:/Users/tmdrb/새파일.txt", "r")
# # # line = f.readline()
# # # print(line)
# # # f.close()
# # # #readeline()을 통해 새파일.txt의 첫 번째 줄 화면에 출력해 줌.

# # # #모든 줄을 화면에 출력하고 싶으면 다음과 같이..
# # # f = open("C:/Users/tmdrb/새파일.txt", 'r')
# # # while True:
# # #     line = f.readline()
# # #     if not line : break
# # #     print(line)
# # # f.close()#더 이상 읽을 줄이 없으면 break를 수행. readline()은 더 이상
# # # #읽을 줄이 없을 때 빈 문자열""을 리턴한다.

# # # while 1:
# # #     data = input()
# # #     if not data : break
# # #     print(data)

# # #readlines 함수 사용하기
# # f = open("C:/Users/tmdrb/새파일.txt", 'r')
# # lines = f.readlines()#readlines()는 파일의 모든 줄을 요소로 갖는 리스트를 돌려준다.
# # for line in lines:
# #     print(line)
# # print(type(lines))

# # #파일에 새로운 내용 추가하기
# # # 쓰기모드로 파일을 열면 그 파일의 내용이 모두 사라짐. 원래 값을 유지하면서 추가만 하고
# # #싶으면 파일추가모드('a')를 쓰면 된다,
# # f = open("C:/Users/tmdrb/새파일.txt", 'a')
# # for i in range(11, 20):
# #     data = "%d번째 줄입니다.\n"%i
# #     f.write(data)
# # f.close()

# #with문을 사용해서 with블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close됨.
# with open("새파일.txt", 'w') as f:
#     f.write("life")

# #sys모듈로 매개변수 주기
# #명령프롬프트 명령어[인수1, 인수2...]같은 느낌으로 진행.
# #sys모듈을 사용하려면 import명령어를 사용해야 한다.->import sys
import sys
args = sys.argv[1:]
for i in args:
    print(i)
