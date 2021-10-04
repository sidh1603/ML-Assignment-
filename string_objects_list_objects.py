#!/usr/bin/env python
# coding: utf-8

# In[49]:


##Answer1

n  =  int(input("enter the value : "))
dot = 1
space = n -1
for i in range(2*n+1):
    if i<n:
        for j in range(space):
            print("",end=" ")
        for j in range(dot):
            print("*",end=" ")
            
        space = space-1
        dot = dot + 1
        print()
        
    elif i == n:
        space = space +1
        dot = dot -1
            
    else:
        space = space + 1
        dot = dot -1
        
        for j in range(space):
            print("",end=" ")
        for j in range(dot):
            print("*",end=" ")
            
        print()
        
            
            
        
    


# In[2]:


##Answer2

name = input("Enter your name : ")
def reverse_funct(name):
    name = name[::-1]
    print(name)
    
reverse_funct(name)

