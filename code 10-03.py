def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num - 1)
print(addNumber(10))

#-------------------------- 위아래 같은 모두 1부터 10까지 더하는 코드
sum = 0
for i in range(11):
    sum += i
print(sum)