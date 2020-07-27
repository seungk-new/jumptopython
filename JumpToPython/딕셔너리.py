#!/usr/bin/env python
# coding: utf-8

# ### 딕셔너리

# In[1]:


a ={1: 'a'}
a[2] = 'b'
a


# In[2]:


a['name'] = 'pey'
a


# In[3]:


del a[1]
a


# In[4]:


del a[2]
a


# In[6]:


grade = {'pey' : 10, 'julliet' : 99}
grade['pey']


# In[10]:


grade['julliet']


# In[13]:


a = {1 : 'a', 2 : 'b'}
a[1]


# In[14]:


a[2]


# In[16]:


dic = {'name':'pey', 'phone': 119990232, 'birth':'1118'}
dic['name']


# In[17]:


a = {1 : 'a', 1 : 'b'}
a


# In[18]:


a = {[1, 2] : 'hi'}


# In[20]:


a = {'name' : 'pey', 'phone' : 11939293, 'birth' : '1118'}
a.keys()


# In[22]:


for k in a.keys():
    print(k)


# In[23]:


list(a.keys())


# In[24]:


a.values()


# In[25]:


a.items()


# In[26]:


a.clear()


# In[27]:


a


# In[28]:


a = {'name' : 'pey', 'phone': '0102829392', 'birthj' : '1118'}
a.get('name')


# In[29]:


a.get('phone')


# In[30]:


a.get('foo', 'bar')


# In[34]:


a = {'name':'pey', 'phone' : '010288281', 'birth' : '1222'}
'name' in a


# In[36]:


'email' in a


# In[ ]:




