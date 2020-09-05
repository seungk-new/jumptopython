#!/usr/bin/env python
# coding: utf-8

# ### 문자열

# In[2]:


a = 'Life is too short'
len(a)


# In[3]:


a[3]


# In[4]:


a[0:4]


# In[6]:


a = '20010331Rainy'
date = a[:8]
date


# In[7]:


weather = a[8:]
weather


# In[8]:


a = 'Pithon'
a[0] + 'y' + a[2:]


# In[9]:


"I ate %d apples" %3


# In[10]:


'I eat %s apples.' %'five'


# In[11]:


number = 3
"I ate %d apples" %number


# In[13]:


number = 3
day = "three"
"I ate %d apples. so I was sick for %s days" %(number, day)


# In[14]:


"Error is %d%%." %98


# In[20]:


'{0:>10}'. format('hi')


# In[21]:


'%10s' %'hi'


# In[22]:


'%-10s' %'hi'


# In[23]:


'%0.4f' %3.42312312313


# In[27]:


'%10.4f' %3.1231


# In[28]:


"I eat {0} apples.". format(3)


# In[31]:


"I eat {0} apples.".format("five")


# In[32]:


number = 3
"I eat {0} apples.". format(number)


# In[38]:


number = 10
day = "three"
"I eat {0} apples. so I was sick for {1} days.". format(number, day)


# In[39]:


"I ate {number} apples. so I was sick for {day} days". format(number= 3, day = "three")


# In[41]:


"I ate {0} apples. so I was sick for {day} days.". format(3, day = 6)


# In[42]:


'{0:<10}'. format('hi')


# In[44]:


'{0:!<10}'. format('hi')


# In[45]:


"{0:=^10}". format("hi")


# In[46]:


"{0:!<10}". format("hi")


# In[50]:


y = 3.314342324
"{0:!<10.4f}". format(y)


# In[52]:


"{{and}}". format()


# In[56]:


"""f문자열 포매팅"""
"""name과 age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있다.
 """
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'


# In[57]:


age = 11
f'나는 내년이면 {age+1}살이 됩니다.'


# In[61]:


"""딕셔너리는 f문자열 포매팅에서 다음과 같이 사용할 수 있다.
딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형이다."""
d = {"name":"홍길동", "age":30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'


# In[63]:


f'{"hi":<10}'


# In[64]:


f'{"hi":!<10}'


# In[65]:


f'{"hi":@^10}'


# In[66]:


y = 3.435323123
f'{y:0.4f}'


# In[67]:


f'{y:>10.4f}'


# In[68]:


f'{{and}}'


# In[69]:


a = "hobby"
a.count('b')


# In[70]:


a = "Python is the best choice"
a.find('t')


# In[71]:


a.find('k')


# In[74]:


a.index('t')


# """index함수와 find함수의 차이점은 찾는 값이 없을 때
# -1을 반환하느냐 애러가 나느냐의 차이"""

# In[77]:


"""문자열 삽입하기
join함수는 문자열 뿐만 아니라 앞으로 배울 리스트나 튜플에서도 가능"""
",".join('abcd')


# In[78]:


",".join(['a', 'b', 'c', 'd'])


# In[87]:


a = 'hi'
a.upper()


# In[88]:


a = 'HI'
a.lower()


# In[89]:


a = '       hi'
a.lstrip()


# In[90]:


a = 'hi            '
a.rstrip()


# In[91]:


a = '        hi          '
a.strip()


# In[92]:


a = "Life is too short"
a.replace("Life", "your leg")


# In[93]:


a = "Life is too short"
a.split()


# In[95]:


b = "a:b:c:d"
b.split(':')


# In[ ]:




