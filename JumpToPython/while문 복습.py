#!/usr/bin/env python
# coding: utf-8

# In[1]:


### While문 복습


# In[8]:


treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")
        # "열 번 찍어 안 넘어가는 나무 없다"


# In[10]:


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """


# In[11]:


number = 0
while number != 4:
    print(prompt)
    number = int(input())
    #number - int(input())은 사용자의 숫자 입력을 받아들이는 것.


# In[ ]:


#while문 강제로 빠져나가기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# In[ ]:


coffee = 10
while True:
    money = int(intput("돈을 넣어 주세요:"))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif moeny > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
    


# In[ ]:


a = 0
while a < 10:
    a = a + 1
    if a% 2 == 0: continue
        print(a)


# In[ ]:


while True:
    print("Ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.")


# In[ ]:




