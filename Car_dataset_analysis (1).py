#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd



# In[5]:


car= pd.read_csv(r"C:\Users\js764\Downloads\2. Cars Data1.csv")


# In[6]:


car.head()


# In[19]:


car.shape


# In[20]:


# find out null value and fill it with columm with mean of that columm #
#data cleaning#


# In[24]:


car.isnull().sum()


# In[31]:


car['Cylinders'].fillna(car['Cylinders'].mean(),inplace=True)


# In[28]:


car


# In[49]:


car.isnull().sum()


# In[48]:


car['Weight'].fillna(car['MPG_Highway'].mean(),inplace=True)
car['Wheelbase'].fillna(car['Wheelbase'].mean(),inplace=True)


# In[ ]:


# what are the differnt types of makes in datasets and counts of each occuerence(make) in data#


# In[ ]:





# In[52]:


car['Make'].value_counts()


# In[ ]:


# show the record where origin is asia or europe #


# In[57]:


car[car['Origin'].isin(['Asia','Europe'])].value_counts('Origin')


# In[ ]:


# remove all the records where weight is above 5000 #


# In[59]:


car['Weight'] > 5000


# In[ ]:


# find out the records where weight is above 5000 # and count of weight car more than 5000kg


# In[63]:


car[car['Weight'] > 5000]. value_counts('Weight')


# In[64]:


# remove all the records where weight is above 5000 # and count of weight car more than 5000kg #


# In[66]:


car[~(car['Weight'] > 5000)]


# # increase the mpg city columm valueby 3 #

# In[7]:


car['MPG_City'].apply(lambda x:x+3)


# In[ ]:




