#!/usr/bin/env python
# coding: utf-8

# In[79]:


### Q1. What is the overall sales trend?
### Q2. Which are the Top 10 products by sales?
### Q3. Which are the Most Selling Products?
### Q4. Which is the most preferred Ship Mode?
### Q5. Which are the Most Profitable Category and Sub-Category?


# IMPORT LIBRARIES

# In[80]:


import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# FOR FIRST 5 ROWS

# In[81]:


df = pd.read_excel(r"C:\Users\28mkt\Documents\Data Analysis  Projects\Sales-Analysis-master\superstore_sales.xlsx")

df.head()


# LAST 5 ROWS

# In[82]:


df.tail()


# In[83]:


df.shape


# In[84]:


df.columns


# In[85]:


df.info()


# In[86]:


df.isnull().sum()


# In[87]:


df.describe()


# ## EXPLORATORY DATA ANALYSIS

# ## What is the overall sales trend?

# In[88]:


df['order_date'].min()


# In[89]:


df["order_date"].max()


# In[90]:


df["month_year"] = df["order_date"].apply(lambda x: x.strftime("%Y-%m"))


# In[91]:


# Getting Month Year from dataset
df["month_year"]


# In[92]:


# Grouping Month Year
df_trend = df.groupby("month_year").sum()["sales"].reset_index()


# In[93]:


# Setting the Figure Sizes
plt.figure(figsize = (15, 6))
plt.plot(df_trend["month_year"], df_trend["sales"], color = "#b80045")
plt.xticks(rotation='vertical', size = 8)
plt.show()


# Which are the Top 10 products by sales?

# In[94]:


# Grouping product name column
prod_sales = pd.DataFrame(df.groupby("product_name").sum()['sales'])


# In[95]:


# Sorting prod_sales column
prod_sales.sort_values("sales", ascending = False)


# In[96]:


# Top 10 by products 
prod_sales[:10]


# ## Which are the Most Selling Products?

# In[97]:


# Grouping product name
most_sell_prod = pd.DataFrame(df.groupby('product_name').sum()["quantity"])


# In[98]:


most_sell_prod = most_sell_prod.sort_values('quantity', ascending = False)


# In[99]:


most_sell_prod[:10]


# Which is the most preferred Ship Mode?

# In[106]:


plt.figure(figsize=(10, 8.5))

sns.countplot(df['ship_mode'])

plt.show()


# In[104]:


##Which are the Most Profitable Category and Sub-Category?


# In[109]:


cat_subcat_profit = pd.DataFrame(df.groupby(['category', 'sub_category']).sum()['profit'])


# In[110]:


cat_subcat_profit.sort_values(['category', 'profit'], ascending = False)

