#!/usr/bin/env python
# coding: utf-8

# ### While문의 기본 구조

# In[11]:


treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")
        


# In[14]:


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())


# In[17]:





# In[19]:


coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee =coffee -1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# In[21]:


a = 0
while a < 10:
    a = a + 1
    if a% 2 == 0: continue
    print(a)


# In[22]:


while True:
    수행할 문장1
    수행할 문장2


# In[ ]:


while True:
    print("Ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.")


# In[ ]:




