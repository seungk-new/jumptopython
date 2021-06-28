# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
#위 코드를 리스트 내포를 사용하여 표현해 보자.
numbers = [1, 2, 3, 4, 5]
result = [num for num in numbers if num % 2 == 1]
print(result)