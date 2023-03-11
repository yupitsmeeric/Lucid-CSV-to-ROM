#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from jinja2 import Environment, FileSystemLoader
from math import log, ceil
import re


# In[12]:


data = pd.read_csv("./rom.csv")
tits = [x  for x in data.columns if x[0]!="#"]


# In[13]:


file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('template.luc')
output = template.render(titles=tits, data = data, 
                         reversed = reversed, re=re, log = log,
                         len = len, ceil=ceil)
print(output)


# In[14]:



with open('testRom.luc', 'w') as file:
    file.write(output)




