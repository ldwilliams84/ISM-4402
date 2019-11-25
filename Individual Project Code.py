#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Load csv file in dataframe
import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


#Find the average number of cars sold
df["Cars Sold"].mean()


# In[14]:


#Store mean in variable csMean
csMean = df["Cars Sold"].mean()
csMean


# In[9]:


#Find and store max cars sold in variable csMax
csMax = df["Cars Sold"].max()
csMax


# In[10]:


#Find and store min cars sold in variabl csMin
csMin = df["Cars Sold"].min()
csMin


# In[53]:


#Find the average number of cars sold per month by gender
#df.groupby("Gender")["Cars Sold"].mean()
pd.pivot_table(df, values=["Cars Sold"], index=["Gender"])


# In[56]:


#Find the avg hours worked by people 
#selling more than 3 cars per month
csTopAvg = df.loc[df["Cars Sold"]>3]["Hours Worked"].mean()
csTopAvg


# In[30]:


#Find the average years of experience and store in variable
csExpAvg = df["Years Experience"].mean()
csExpAvg


# In[31]:


#Find the avg years of experience for people selling more
#than 3 cars
csTopExp = df.loc[df["Cars Sold"]>3]["Years Experience"].mean()
csTopExp


# In[58]:


#Find the avg cars sold per month sorted by whether they
#had sales training
pd.pivot_table(df, values= ["Cars Sold"], index=["SalesTraining"])


# In[91]:


df2 = pd.pivot_table(df, values= ["Years Experience", "Cars Sold"], index=["Gender", "SalesTraining"])
df2


# In[95]:


#Create bar graph showing the relationship between gender/Years Experience and number of avg Cars Sold
df2.plot.bar()


# In[98]:


#Create pivot table for visualization 
df3 = pd.pivot_table(df, values= ["Hours Worked", "Cars Sold"], index = ["Gender"])
df3


# In[105]:


#Create pie chart to show cars sold by males vs females, also show hours worked by males/females
df3.plot.pie(subplots = True)


# In[ ]:




