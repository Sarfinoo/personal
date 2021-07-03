#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import random
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import threading
from datetime import datetime


# In[2]:


# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(10)


# In[3]:


# Open the Website
browser.get('https://ts1.x1.europe.travian.com/login.php')


# In[4]:


# Account login
ts_name = 'Jack_Daniels'
ts_password = 'hfgghf33'






# Open the lists
#browser.get('https://ts1.x1.europe.travian.com/build.php?id=39&gid=16&tt=99')






# In[5]:


# Coockies pop-up (close)

#cookies = browser.find_element_by_xpath('//*[@id="cmpbntnotxt"]') != 0

#if (cookies):
  #  browser.find_element_by_xpath('//*[@id="cmpbntnotxt"]').click();


# In[6]:


browser.find_element_by_name('name').send_keys(ts_name)
browser.find_element_by_name('password').send_keys(ts_password)

browser.find_element_by_id('s1').click();


# In[7]:


browser.find_element_by_xpath("//*[@id='sidebarBoxVillagelist']/div[2]/ul/li[12]/a/span/span").click();

