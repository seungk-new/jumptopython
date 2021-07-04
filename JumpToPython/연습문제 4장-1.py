#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# def is_odd(num):
#     if num % 2 == 1:
#         return True
#     else:
#         return False

# print(is_odd(3))
# print(is_odd(2))

#lambda를 이용한 풀이
is_old = lambda num : True if num % 2 == 1 else False
print(is_old(2))
