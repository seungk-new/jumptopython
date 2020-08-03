#!/usr/bin/env python
# coding: utf-8

# ### for문 복습

# In[2]:


# for 변수 in 리스트(또는 튜플, 문자열):
    #수행할 문장1
    #수행할 문장2
    #...


# In[3]:


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


# In[7]:


a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
    # 이 예는 a리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last)변수에 대입된다.


# In[8]:


# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여 주시오.


# In[10]:


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
# 각각의 학생에게 번호를 붙여 주기 위해 number 변수를 사용하였다,


# In[11]:


# continue문을 만나면 문장 처음으로 돌아가게 된다,


# In[12]:


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)


# In[15]:


# range(10)은 0부터 10 미만의 숫자를 표현하는 range 객체를 만들어 준다.
# range(시작 숫자, 끝 숫자)


# In[14]:


a = range(10)
a


# In[16]:


a = range(1, 11)
a


# In[20]:


add = 0
for i in range(1, 11):
    add = add + i
print(add)


# In[24]:


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


# In[32]:


for i in range(2, 10):
    for j in range(1, 10):
            print(i*j, end =" ")
    print('')
# 매개변수 end를 넣어줌으로써 해당 결괏값을 출력할 때 다음줄로
# 넘어가지 않고 그 줄에 계속 출력
# print('')는 2단, 3단 등을 구분하기 위해 두 번째 for문이 끝나면
# 결괏값을 다음 줄부터 출력하게 해주는 문장이다.


# In[33]:


# 리스트 안에 for문을 포함하는 리스트 내표를 사용하면 좀 더 직관적


# In[35]:


a = [1, 2, 3, 4]
result =[]
for num in a:
    result.append(num*3)
print(result)
# a리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담는 예제


# In[36]:


a = [1, 2, 3, 4]
result = [num*3 for num in a if num%2 == 0]
print(result)


# In[37]:


# [1, 2, 3, 4]중에서 짝수에만 3을 곱하여 담고 싶다면 리스트 내포 안에 if조건 사용


# In[40]:


a = [1, 2, 3, 4]
result = [num*3 for num in a if num %2 == 0]
print(result)


# In[ ]:




