#!/usr/bin/env python
# coding: utf-8

# ### 집합 자료형

# In[1]:


s1 = set([1, 2, 3])
s1


# In[2]:


s2 = set("Hello")
s2


# In[3]:


s1 = set([1, 2, 3])
l1 = list(s1)
l1


# In[5]:


l1[0]


# In[6]:


t1 = tuple(s1)
t1


# In[7]:


t1[0]


# In[8]:


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])


# In[10]:


s1 & s2


# In[11]:


s1.intersection(s2)


# In[12]:


s1 | s2


# In[15]:


s1.union(s2)


# In[16]:


s1 - s2


# In[17]:


s2 - s1


# In[18]:


s1.difference(s2)


# In[19]:


s2. difference(s1)


# In[20]:


s1 = set([1, 2, 3])
s1.add(4)
s1


# In[24]:


s1 = set([1, 2, 3])
s1.add(4)
s1


# In[25]:


s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1


# In[26]:


s1 = set([1, 2, 3])
s1.remove(2)
s1


# In[ ]:




