#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px
import re
from io import BytesIO
import requests
import json
from urllib.parse import urlencode
import gspread
import math as math
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
df=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/Pokemon.csv')
df


# In[2]:


df.rename(columns={'#':'id'})


# In[3]:


# изменим названия исходных столбцов:
f = lambda x : x.lower().replace(' ', '_').replace('.','')
df=df.rename(columns={'#':'id'})
df=df.rename(columns=f)
df


# In[4]:


legends=df.groupby('generation').agg({'legendary': 'value_counts'}).rename(columns={'legendary':'count'}).reset_index()
legends


# In[5]:


# используем unstack, чтобы поместить уровень индекса legendary в уровень оси столбцов
legends=df.groupby('generation').legendary.value_counts().to_frame()
legends=legends.rename(columns={'legendary':'legendary_count'})
legends_unstacked=legends.unstack(level='legendary')
legends


# In[6]:


df


# In[47]:


# Сгруппируем датасет pokemon по переменным generation и type_1, посчитаем количество легендарных покемонов внутри групп

df1=df.groupby(['generation', 'type_1']).legendary.value_counts().to_frame().rename(columns={'legendary':'legendary_count'}).sort_values('legendary_count',ascending = False)
# df2=df1.unstack(level='legendary')
df1[0:50]


# In[7]:


avocado_agg = pd.DataFrame({'type' : ['conventional', 'organic'],
                            'AvgPrice_2015' : [1.077963, 1.673324],
                            'AvgPrice_2016' : [1.105595, 1.571684],
                            'AvgPrice_2017' : [1.294888, 1.735521],
                            'AvgPrice_2018' : [1.127886, 1.567176],
                            })
avocado_agg


# In[58]:


lng = pd.wide_to_long(avocado_agg, ['AvgPrice'], i=['type'], j='year', sep='_')
lng


# In[8]:


# Считаем данные 
sup=df=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/superheroes_power_matrix.csv')
sup


# In[76]:


superheroes_long=sup.melt(id_vars=['Name'],  var_name='superpower', value_name='value')
superheroes_long


# In[77]:


aa=superheroes_long.loc[superheroes_long.value == True]


# In[80]:


superheroes_powers=aa.groupby('Name').superpower.apply(list).to_frame().reset_index()


# In[81]:


superheroes_powers


# In[ ]:




