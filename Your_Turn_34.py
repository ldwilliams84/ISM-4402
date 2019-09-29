#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Load dataset into Panda
import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]

# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']

# categorizes the column grade based on the bins list
df['lettergrade'] = pd.cut(df['grade'], bins, labels=group_names)
df


# In[15]:


#Create bin dividers
bins2 = [0, 80, 100]
#categorize pass or fail based on the bins2 list
pass_or_fail = ['Fail', 'Pass']
df['pass_fail'] = pd.cut(df['grade'], bins2, labels=pass_or_fail)
df


# In[ ]:




