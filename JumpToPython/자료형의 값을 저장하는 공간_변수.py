#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1
b = "python"
c = [1, 2, 3]


# In[3]:


a = [1, 2, 3]
id(a)


# In[4]:


a = [1, 2, 3]
b = a
id(a)


# In[5]:


id(b)


# In[6]:


a is b


# In[7]:


a is not b


# In[8]:


a[1] = 4
a


# In[9]:


b


# In[10]:


a = [1, 2, 3]
b= a[:]
a[1] = 4
a


# In[11]:


b


# In[12]:


from copy import copy
b = copy(a)


# In[13]:


b is a


# In[14]:


a is b


# In[16]:


a          is b


# In[18]:


a, b = ('Python', 'Life')


# In[19]:


(a, b) = 'Python', 'Life'


# In[20]:


[a, b] = ['Python', 'Life']


# In[21]:


a = b = 'Python'


# In[22]:


a = 3
b = 5
a, b = b, a
a


# In[23]:


b


# In[ ]:




