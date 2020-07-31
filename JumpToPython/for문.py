#!/usr/bin/env python
# coding: utf-8

# In[2]:


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


# In[5]:


a = [(1, 2), (3, 4), (5, 6)]
for(first, last) in a:
    print(first % last)


# In[7]:


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark > 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)


# In[11]:


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)


# In[14]:


a = range(10)
a
#0부터 10까지의 숫자를 데이터로 갖는 객체, 마지막 숫자는 포함되지 않는다.


# In[15]:


makrs = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
        print("%d번 학생 축하합니다. 합격입니다." %(number + 1))


# In[16]:


for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end="")
    print('')


# In[18]:


a = [1, 2 ,3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)


# In[19]:


a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)


# In[20]:


a = [1, 2, 3, 4]
result = [num*3 for num in a if num%2 == 0]
print(result)


# In[25]:


result = [x*y for x in range(2, 10)
for y in range(1, 10)]
print(result)


# In[ ]:




