#!/usr/bin/env python
# coding: utf-8

# ### 무작위 복습

# In[5]:


#인덱싱
a = "life is too short, you need python"
b = a[0] + a[1] + a[2] + a[3]
b


# In[7]:


# 슬라이싱
a = "life is too short, you need python"
a[0:4]#첫자리는 0이고 끝자리는 포함 안한다.


# In[10]:


#문자열 포매팅
"I eat %d apples." %3 # %d를 문자열 포맷코드라고 한다.


# In[14]:


"I eat %s apples" %'five' # 문자열을 삽입하기 위해서는 %s사용


# In[15]:


number = 3
"I eat %d apples." %number


# In[16]:


number = 10
day = "three"
"I ate %d apples. so I was sick for %s days" %(number, day)


# In[18]:


"%10s" %"hi" # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽 정렬 앞은 공백으로 남겨라


# In[19]:


"%0.4f" % 3.1232141242


# In[21]:


"%10.11f" %5.55223423422342


# In[22]:


# 문자열 개수 세기(count)
a = "hobby"
a.count('b')


# In[23]:


# 위치 알려주기1 (find)
a = "python is the best choice"
a.find('b')


# In[26]:


a.find('k') # 찾는 문자열이 존재하지 않으면 -1을 반환


# In[28]:


# 위치 알려주기2 (index)
a = "life is too short"
a.index('t')


# In[30]:


a.index('z') #해당 문자열 없으면 오류 발생


# In[34]:


# 소문자를 대문자로 바꾸기
a = 'hi'
a.upper()


# In[35]:


# 대문자를 소문자로 바꾸기
a = "HI"
a.lower()


# In[36]:


# 왼쪽 공백 지우기
a = " hi"
a.lstrip()


# In[37]:


# 오른쪽 공백 지우기
a = "hi   "
a.rstrip()


# In[41]:


#양쪽 공백 지우기
a = "                hi                   "
a.strip()


# In[42]:


# 문자열 바꾸기
a = "life it too short"
a.replace('life', 'your leg')


# In[45]:


# 문자열 나누기
a = "life is too short"
a.split()
#split함수에 아무것도 넣지 않으면 공백을 기준으로 나눠준다.
['life', 'is', 'too', 'short']


# In[46]:


a = "lfie:is:too:short"
a.split(":") #split함수 쓸 때 :를 넣어주면 :기준으로 나눠줌


# In[ ]:




