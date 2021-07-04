#for문을 사용하여 중간고사 평균 구하기
grade = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for i in grade:
    result += i
result /= len(grade)
print(result)