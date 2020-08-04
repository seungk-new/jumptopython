#!/usr/bin/env python
# coding: utf-8

# ### while if for문 연습문제

# In[ ]:


# 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")


# In[23]:


# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합 구하기
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i # i가 1000이하일 동안 i를 3으로 나눠서 나머지가 0이면 i를 모두 더한다.
    i = i + 1
print(result)


# In[8]:


#while문을 사용하여 다음과 같은 별(*)을 표시하느 프로그램 작성
i = 0
while True:
    i += 1 #while문 수행 시 1씩 증가
    if i > 5: break #i의 값이 5 이상이면 while문은 벗어난다.
    print('*' * i) #i 값의 개수만큼 *를 출력한다.


# In[9]:


# for문을 사용해 1부터 100까지의 숫자를 출력해보자
   for i in range(1, 101):
       print(i)


# In[ ]:


#for문을 사용하여 A학급의 평균 점수를 구해보자
A = [70, 60, 65, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score #A학급의 점수를 모두 더한다.
average = total/len(A) #평균 구하기 위해 총점수를 총학생수로 나눔
print(average)


# In[ ]:


numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)


# In[ ]:


numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)


# In[1]:


numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)


# In[4]:


numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(i)


# In[5]:


result = 0
i = 1
while i <=1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)


# In[10]:


for i in range(1, 101):
    print(i)


# In[22]:


A = [78, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total = total + score
    #total = total + score
average = total / len(A)
print(average)


# In[24]:


numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)


# In[27]:


# 리스트 중에서 홀수에만 2를 곱하여 저장하는 위와 같은 코드가 있다.
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)


# In[ ]:




