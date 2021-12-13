#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Answer 1

class Area:
    global s  
    s = int(input())
    global a 
    a = int(input())
    global b 
    b = int(input())
    global c 
    c = int(input())

    def __init__(self, s, a, b, c):
        self.s = s
        self.a = a
        self.b = b
        self.c = c
        
class Area1(Area):
    def __init__(self,*args):
        Area.__init__(self,*args)
    def calculate_area(self):
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("the area of triangle is : " , area)

obj = Area1(s,a,b,c)
obj.calculate_area()


# In[2]:


#### Answer2
a = []
x = input()
word_list = x.split(' ')
result = list(word_list)
#print(result)

b = []
n = input()
integer_list = n.split(' ')
result1 = list(integer_list)
#print(result1)

for i in range(len(result)):
    print(result[i])
    
for j in range(len(result1)):
    print(result1[j])


if(len(result[i]) > len(result1[j])):
    a.append(result[i])
    print(a)
else:
    b.append(result1[j])
    print(b)


# In[3]:





# In[6]:


##Answer2
def filter_long_words():
    a = []
    x = input()
    word_list = x.split(' ')
    result = list(word_list)
    n = int(input())
    for i in range(len(result)):
        if(len(result[i]) > n):
            a.append(result[i])
            print(a) 
        

filter_long_words()


# In[7]:


##Answer3
def length_words():
    l = []
    word = input()
    word_list = word.split(' ')
    result = list(word_list)
    
    for i in range(len(result)):
        l.append(len(result[i]))
        print(l)
        
length_words()


# In[8]:


##Answer4
def character_words():
    word = input()
    vowel = ['a','e','i','o','u']
    for i  in word:
        if i in vowel:
            return True
        else:
            return False
    
character_words()

