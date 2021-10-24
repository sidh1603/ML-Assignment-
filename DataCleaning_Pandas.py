#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[3]:


df


# ##Answer1

# In[4]:



df['FlightNumber'] = df['FlightNumber'].fillna(0)


# In[5]:


type(df['FlightNumber'])


# In[6]:


df['FlightNumber'] = (df['FlightNumber'] + 10).astype(int)


# In[7]:


df['FlightNumber']


# ##Answer2

# In[8]:


df


# In[9]:


#df = df['From_To'].str.split('_').str[0]


# In[10]:


tmpDF = pd.DataFrame(columns=['From','To'])
tmpDF[['From','To']] = df['From_To'].str.split('_', expand=True)


# In[11]:


tmpDF


# ##Answer3

# In[12]:


#tmpDF['From'][0]

tmpDF['From'] = tmpDF['From'].str.capitalize()
tmpDF['To'] = tmpDF['To'].str.capitalize()


# In[13]:


tmpDF


# In[14]:


df = df.drop(['From_To'],axis=1)


# In[15]:


df


# In[16]:


frames = [df, tmpDF]

df = pd.concat((frames),axis=1)


# In[17]:


df


# ##Answer5

# In[18]:


#x = result['RecentDelays'].tolist()

delays = pd.DataFrame(df['RecentDelays'].tolist(),columns=['delay_1','delay_2','delay_3'])
delays
# display the resulting df


# In[19]:


#result['RecentDelays'] = result['RecentDelays'].str.strip(",").str.split(',')
#result= result['RecentDelays'].tolist()


# In[20]:


rep = [df,delays]


# In[21]:


df = pd.concat((rep),axis=1)


# In[22]:


df


# In[23]:


df = df.drop(["RecentDelays"],axis=1)


# In[24]:


df

