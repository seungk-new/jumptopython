# -*- coding: utf-8 -*-
"""210803lesson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uOsjl2wy99CcBCYQU_OxsjkPVhTYphrV

> 
    test1.py 상수 변수 함수 클래스 ex) 프런트쪽

    test2.py 상수 변수 함수 클래스 ex) DB쪽

    test3.py 상수 변수 함수 클래스 ex) 백엔드쪽

* 모듈을 사용하는 이유
>     1 코드 작성과 관리
      2 이미 작성된 코드 재사용
      3 공동작업이 편리

* MSA(Micro Service Architecture)
    >   __회원관리__
        회원등록(모듈)
        회원검색(모듈)
        회원수정(모듈)
        회원탈퇴(모듈)

        -> 각각의 모듈을 만드는 생각

* 내장 마술 명령어(magic command)
    * %%writefile을 이용해 코드를 파일로 저장
    
    
    코드 셀의 코드를 파이썬 코드 파일로 저장하기 
    -> %%writefile [-a] file.py
     
    저장된 파이썬 코드 파일 불러오기
    -> %%load file.
    
    파이썬 코드 파일 실행하기
    -> %%run file.py
"""

# Commented out IPython magic to ensure Python compatibility.
# # 모듈을 만들고
# %%writefile my_first_module.py
# 
# def my_function():
#     print("This is my first module")

# 모듈이 생성되었는지 확인
!cat my_first_module.py

# 모듈 불러오기
# import 모듈명 
# 모듈을 import한 후에는 '모듈명.변수', '모듈명.함수()', 모듈명.클래스()와 같은 형식으로 모듈에서 정의한 내용을 사용'''

"""> import를 한다.

    메모리에 올린다~
> install을 한다.

    내 피씨에 설치를 한다~
"""

import my_first_module
my_first_module.my_function()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_area.py
# 
# PI = 3.14
# def square_area(a):
#     return a ** 2
# 
# def circle_area(r):
#     return PI * r ** 2

import my_area
print('정사각형 넓이:', my_area.square_area(2))

import my_area
print('원의 넓이:',int(my_area.circle_area(10)))

# 불러온 모듈에서 사용할 수 있는 변수, 함수, 클래스를 알고 싶다면 
# dir(모듈명)을 이용

dir(my_area)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_second_module.py
# 
# def smile(a):
#     return '^' * a

import my_second_module
my_second_module.smile(9)

""">tip: 코랩에서 모듈 작성하시고 파일 저장하신 후 이후 수정하시게되면,  반영이 안되는 경우가 있어요.
코드 문제없으시면
런타임 초기화 하시고 다시 처음부터 실행해보세요.

* 모듈 내에 있는 변수 함수 클래스를 '모듈명.' 없이 변수 함수() 클래스()처럼 직접 호출해서 사용할 수 있음.

    from 모듈명 import 변수명

    from 모듈명 import 함수명

    from 모듈명 import 클래스명
"""

from my_second_module import * # *은 모듈 내의 모든 변수, 함수, 클래스르 불러오는 것
smile(2)

from my_area import PI

print('pi:', PI)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_module1.py
# 
# def func1():
#     print("func1 in my_module1")
# def func2():
#     print("func2 in my_module1")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_module2.py
# 
# def func2():
#     print("func2 in my_module2")
# def func3():
#     print("func3 in my_module2")

from my_module1 import *
from my_module2 import *

func1()
func2() # my_module1과 my_module2에 있는 func2()는 나중에 선언해서 불러온 모듈의 함수가 호출됨.
func3()

"""* 모듈명을 별명으로 선언
    
    import 모듈명 as 별명

    코드 작성할 때
    별명.변수 별명.함수 별명.클래스처럼 지정할 수 있음
    

"""

import my_area as area

print('pi=', area.PI)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_module_test1.py
# def func(a):
#     print("입력 숫자: ", a)
# 
# func(3)

# Commented out IPython magic to ensure Python compatibility.
# %run my_module_test1.py

import my_module_test1

#모듈에서 직접 수행하는 경우와 임포트해서 이용하는 경우 구분해서 사용
# 임포트할 때는 if__name__=='__main__': 안의 코드가 실행되지 않음.
# if__name__=='__main__':
    # <직접 수행할 때만 실행되는 코드>
# else:
    #   <임포트 했을 때만 실행되는 코드>

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_module_test3.py
# 
# def func(a):
#     print("입력숫자:", a)
# 
# if __name__=='__main__':
#     print("모듈을 직접 실행했을 때 실행")
#     func(3)
#     func(4)
# else:
#     print("모듈을 임포트해서 실행했을 때 출력")

# Commented out IPython magic to ensure Python compatibility.
# %run my_module_test3.py

import my_module_test3

# random함수를 임포트 하면 난수를 생성할 수 있음(0~1사이의 임의의 실수를 생성한다.)
import random
round(random.random(),2)

import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print('주사위 두 개의 숫자: {0},{1}'.format(dice1,dice2))

import random
random.randrange(1, 10, 3) # 1<=정수<=10범위에서 3만큼 건너띄면서 임의의 정수 반환

random.randint(1,6) # 1이상 6이하에서 임의의 정수 한 개 반환

random.sample([1,3,4,1,5,10],2) # 시퀀스로 이뤄진 모집단(population)에서 중복되지 않는 임의의 인자 2개를 반환

random.choice([1,2,3]) # 공백이 아닌 시퀀스에서 임의의 항목을 반환