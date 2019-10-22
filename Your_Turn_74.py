#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[14]:


import matplotlib.pyplot as plt
df.plot()
displayText = "Wow!"
xloc = 0.0
yloc = df['Grades'].min()
xtext = 1
ytext = -150
plt.annotate(displayText, 
            xy=(xloc, yloc), 
            arrowprops=dict(facecolor='black', shrink=0.05),   
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')


# In[ ]:




