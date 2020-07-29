#!/usr/bin/env python
# coding: utf-8

# ### 조건문  if

# In[4]:


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    


# In[6]:


money = True
if money:
    print("1")
else:
    print("2")


# In[7]:


x = 3
y = 2
x > y


# In[8]:


x == y


# In[9]:


x != y


# In[13]:


money = 2000
if money >=3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# In[15]:


money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# In[16]:


x in 리스트
x not in 리스트
x in 튜플
x not in 튜플
x in 문자열
x not in 문자열


# In[17]:


1 in [1, 2, 3]


# In[18]:


1 not in [1, 2, 3]


# In[19]:


'a' in ('a', 'b', 'c')


# In[22]:


'J' not in ('A', 'B', 'C')


# In[25]:


pocket = ['paper', 'money', 'cellphone']
if 'mouse' in pocket:
    pass
else:
    print("카드를 꺼내라")


# In[30]:


pocket = ['paper', 'handphone']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")


# In[32]:


pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')


# In[33]:


if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')


# In[34]:


pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print('카드를 꺼내라')


# In[45]:


if score >= 60:
    message = "success"
else:
    message = "failure"


# In[42]:


message = "success" if score >= 60 else "failure"


# In[ ]:


조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

