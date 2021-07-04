result = 0
def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))

2대의 계산기가 필요한 상황에서 각 계산기는 각각의 결괏값을 유지해야 하기 때문에
위와 같이 add함수 하나만으로는 결괏값을 따로 유지할 수 없다.
result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2
print(add1(1))
print(add1(4))
print(add2(3))
print(add2(7))


