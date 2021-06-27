#!/usr/bin/env python
# coding: utf-8

# ### if문 복습

# In[3]:


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# In[4]:


x = 3
y = 2
x > y


# In[6]:


x==y


# In[9]:


money = 4000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# In[10]:


# x or y - x와 y 둘 중 하나만 참이어도 참이다.
# x and y - x와 y 모두 참이어야 한다.
# not x - x가 아니면 참이다.


# In[11]:


money = 2000
card = True
if money >=3000 or card:
        print("택시를 타고 가라")
else:
    print("걸어 가라")


# In[12]:


1 in [1, 2, 3]


# In[14]:


1 not in [1, 2, 3]


# In[15]:


'a' in ('a', 'b', 'c')


# In[17]:


'j' not in ('a', 'b', 'c')


# In[23]:


pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


# In[27]:


pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")


# In[29]:


pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
    #elif는 이전 조건문이 거짓일 때 수행된다.


# In[32]:


if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")


# In[34]:


pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
#if문 뒤에 수행할 문장을 콜론(:)뒤에 적어줘서 덜 복잡해 보임


# In[36]:


if score >= 60:
    message = "success"
else:
    message = "failure"
# socre가 60 이상일 경우 message에 문자열 "success"를, 아닐 경우에는 "failure"를 대입하는 코드


# In[38]:


message = "success" if score >= 60 else "faulure"
#파이썬 조건부 표현식(conditional expression)을 사용하면 간단하게 표현 가능


# In[39]:


#조건부 표현식
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우


# In[ ]:




