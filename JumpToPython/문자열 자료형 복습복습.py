#!/usr/bin/env python
# coding: utf-8

# ### 문자열 자료형 2회독

# In[2]:


"hello world"


# In[3]:


'python is fun'


# In[4]:


"""Life is too short, you need python"""


# In[5]:


'''Life is too short, you need python'''


# In[6]:


food = "python's favorite food is perl"


# In[7]:


food = 'pythone's~~~~
# 작은 따옴표 안에 작은 따옴표는 'python'이 문자열로 인식되는 오류


# In[8]:


'"python is very easy."he says'


# In[9]:


food = 'python\'s favorite is perl'


# In[10]:


say = "\"python is very easy.\"he says"


# In[11]:


say = "\"python is very easy.\"he says"


# In[13]:


Life is too short
You need python
#문자열은 이렇게 두 줄짜리도 있을 수 있다. 이땐 이스케이프 코드\n 삽입하기.


# In[15]:


multiline = "Life is too short\n You need python"


# In[21]:


multiline = '''
Life is too short
You need python
'''


# In[22]:


multiline ="""
Life is too short
You need python
"""


# In[23]:


print(multiline)


# In[24]:


# \N 문자열 안에서 줄을 바꿀 때 사용
# \t 문자열 사이에 탭 간격을 줄 때 사용
# \\ 문자 \를 그대로 표현할 때 사용
# \' 작은 따옴표를 그대로 사용할 때 사용
# \" 큰 따옴표를 그대로 표현할 때 사용
# \r 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a 벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다.)
# \b 백스페이스
# \000 널문자


# In[25]:


# \N, \t, \\, \', \" 를 가장 많이 사용한다


# In[28]:


head = "python"
tail = "is fun!"
head + tail


# In[29]:


a = "python"
a * 2


# In[30]:


a = "Life is too short"
len(a)


# In[31]:


a = "Life is too short, You need python"


# In[32]:


Life is too short, You need python


# In[33]:


a = "Life is too short, You need python"
a[3]


# In[34]:


# 인덱싱(무언가를 가리킨다는 뜻) 슬라이싱은 (무언가를 잘라낸다는 뜻)


# In[35]:


a = "Life is too short, You need python"
a[0]


# In[37]:


a[-1]


# In[ ]:




