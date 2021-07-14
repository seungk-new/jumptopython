#try, except를 통해 예외적으로 오류를 처리할 수 있다.
#try:
    #수행할 문장
#except[발생 오류[as 오류 메시지 변수]]:
#try블록 수행 중 오류가 발생하면 except블록이 수행된다. 하지만 try블록에서 오류가
#발생하지 않으면 except블록은 수행되지 않는다.
#except구문의 []기호는 괄호 안의 내용을 생략할 수 있다는 관례적인 표기법임.
#except구문은 try, except 두개 쓰는 방법, 발생 오류만 포함한 except문(이 경우 미리 정해 놓은 오류 이름과 일치할 때만 except블록을 수행함)
#발생 오류와 오류 메시지 변수까지 포함한 except문 3가지 방식 사용가능.
# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)
#try문에 finally절을 사용할 수 있다.
#try문 수행 도중 예외 발생 여부에 상관없이 항상 수행. finally절은
#사용한 리소스를 close해야 할 때에 많이 사용한다.
f = open('foo.txt', 'w')
# try:
#     #수행할 문장
# finally:
#     f.close
