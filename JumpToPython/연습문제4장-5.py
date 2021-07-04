f1 = open("test.txt", 'w')
f1.write("life is too short")
f2 = open("test.txt", 'r')
print(f2.read())
#이렇게 하면 life is too short라는 문장을
#출력하지 않는다.
#f1.close()를 통해서 열린 객체를 먼저 닫아줘야 함.
#파일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를
#읽을 수 없다. 열린 파일 객체를 close로 닫아준 후 다시
#열어서 파일의 내용을 읽어야 한다.
#굳이 close를 하고 싶지 않으면 with구문을 사용한다.
with open("test.txt", 'w') as f1:
    f1.write("life is too short")
with open("test.txt", 'r') as f2:
    print(f2.read())