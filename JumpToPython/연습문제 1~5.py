#!/usr/bin/env python
# coding: utf-8

# ###연습문제

# In[20]:


"""1번"""
a = 80
b = 75
c = 55
(a+b+c)/3


# In[52]:


"""2번"""
a = 13
if a % 2 == 0:
    print("짝수")
else:
    print("홀수")


# In[54]:


"""3번"""
pin = "881120-1068234"
pin[:6]


# In[56]:


pin[7:]


# In[58]:


yyyymmdd = pin[:6]
print(yyyymmdd)


# In[59]:


num = pin[7:]
print(num)


# In[60]:


"""4번"""
pin = "881120-1068234"
print(pin[7])


# In[19]:


"""5번"""
a = "a:b:c:d"
a.replace(":", "#")


# In[62]:


a = "a:b:c:d"
b = a.replace(":", "#")
print(b)


# In[ ]:




