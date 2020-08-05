#!/usr/bin/env python
# coding: utf-8

# ### 함수

# In[1]:


def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>


# In[2]:


def add(a, b):
    return a + b
#이 함수의 이름은 add이고 2개의 값을 입력받으며 결과값은 2개의 입력값을 더한 값이다.


# In[4]:


def add(a, b):
    return a + b


# In[5]:


a = 3
b = 4
c = add(a, b)
print(c)


# In[6]:


#매개변수와 인수의 차이를 알고 가자
def add(a, b): #a, b는 매개변수
    return a + b
print(add(3, 4)) #3, 4는 인수


# In[7]:


def add(a, b):
    result = a + b
    return result
#입력값과 결과값이 있는 함수


# In[8]:


a = add(3, 4)
print(a)
#결과값을 받을 변수 = 함수이름(입력인수1, 입력인수2)


# In[9]:


def say():
    return 'HI'
# 입력값이 없는 함수


# In[13]:


a = say()
print(a)
# 입력값이 없는 함수=> 결과값을 받을 변수 = 함수이름()


# In[14]:


def add(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))
    #결과값이 없는 함수


# In[15]:


add(3, 4)


# In[16]:


a = add(3, 4)
print(a)


# In[17]:


# 입력값도 결과값도 없는 함수
def say():
    print('HI')


# In[18]:


say()


# In[20]:


#매개변수 지정하여 호출하기
def add(a, b):
    return a + b


# In[21]:


result = add(b=5, a=3)
print(result)


# In[22]:


#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def함수이름(*매개변수):
    <수행할 문장>


# In[27]:


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


# 

# In[31]:


reult = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


# In[35]:


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
        return result


# In[33]:


result = add_mul('add', 1,2,3,4,5)
print(result)


# In[36]:


result = add_mul('mul', 1,2,3,4,5)
print(result)


# In[37]:


def print_kwargs(**kwargs):
    print(kwargs)


# In[39]:


print_kwargs(a=1)
{'a' : 1}
print_kwargs(name='foo', age = 3)
{'age' : 3, 'name' : 'foo'}

#딕셔너리로 만들어 출력해주는 **


# In[41]:


def add_and_mul(a, b):
    return a + b, a*b
#add_and_mul함수는 2개의 입력 인수를 받아 더한 값과 곱한 값을 돌려주는 함수이다.


# In[42]:


result = add_and_mul(3, 4)


# In[43]:


result


# In[45]:


result1, result2


# In[56]:


#return으로 함수 빠져나가기
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)


# In[53]:


say_nick('야호')


# In[57]:


say_nick("바보")


# In[58]:


def say_myself(name, old, man=True): #매개변수의 초기값을 man=True설정
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


# In[65]:


say_myself("박응용", 27)


# In[66]:


a = 1
def vartest(a):
    a = a + 1


# In[68]:


vartest(a)
print(a)
#함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다.


# In[71]:


#함수 안에서 함수 밖의 변수를 변경하는 방법(return사용)
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)


# In[72]:


#함수 안에서 함수 밖의 변수를 변경하는 방법(global사용)
a = 1
def vartest():
    global a
    a = a + 1
vartest()
print(a)


# In[79]:


#lambda는 def를 사용할 수 없거나 사용해야할 정도로 복잡하지 않을 때
add = lambda a, b: a+b
result = add(3, 4)
print(result)
#lambda로 만들 함수는 return명령어 없어도 결과값을 돌려준다.


# In[ ]:




