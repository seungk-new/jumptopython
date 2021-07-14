# #while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합 구하기.
# s = 0
# i = 1
# while 1 <= i <= 1000:
#     if i % 3 == 0:
#         s = s + i
#     i = i + 1 # i는 if문과 상관없이 while문이 진행되는 동안 1씩 증가해야 하므로 if문과 동일한 indent적요이함.
# print(s)

# #while문을 사용하여 *을 찍어내기
# i = 0
# while i < 5:
#     i = i + 1
#     print(i * '*') #i가 5보다 작을 동안 계속해서 i의 개수만큼 *을 찍어냄, 그래서 while문 안에 print가 들어감.

# #for문을 사용해서 1부터 100까지의 숫자 출력하기
# for i in range(1, 101):
#     print(i, end = ', ') #한 줄로 출력하고 싶으면 end =''해주고 ''안에 뭔가 넣으면 그것도 같이 표현 됨.

# #A학급에 총 10명의 학생이 있음. 중간고사 점수의 평균 for문 이용해 구하기.
g = [70, 60, 55, 75, 95, 90, 80, 80 ,85, 100]
# i = 0
# s = 0
# while i < len(g):
#     for i in range(len(g)):
#         i = i + 1
#         s = s + g[i-1]
#     average_g = s/len(g)
# print(average_g)
# 다른 풀이..
b = 0
result = 0
while b < len(g):
    result += g[b]
    b += 1 
result /=  len(g)
print(int(result))