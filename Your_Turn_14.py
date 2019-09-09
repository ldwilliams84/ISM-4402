#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
from sqlalchemy import create_engine

#Connect to sqlite db
db_file = r'datasets/sales_data.db'
engie = create_engine("sqlite:///{}".format(db_file))

sql = 'SELECT * from test where Grades > 80'

sales_data_df = pd.read_sql(sql, engine,)
sales_data_df.head()


# In[ ]:




