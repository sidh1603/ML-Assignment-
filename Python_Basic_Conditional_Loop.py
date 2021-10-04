#!/usr/bin/env python
# coding: utf-8

# In[8]:


##Answer1

def number():
    for i in range(2000,3201):
        if i % 7 == 0 and i%5 !=0:
            print(i, end =",")

number()


# In[46]:


##Answer2

def name(fname,lname):
    fname = fname[::-1]
    lname = lname[::-1]
    fname = fname.split('  ')
    lname = lname.split('  ')
    f_name = fname + lname
    print(f_name[::-1])


    #f_name = list(reversed(f_name))
    #print(f_name)
    
name("sidd" ,"rana")


# In[49]:


##Answer3

def volume(d):
    r = d/2
    v = 4/3*(3.14*(r**3))
    print(v)
    
volume(12)


# In[ ]:




