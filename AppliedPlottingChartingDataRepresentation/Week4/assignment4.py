#!/usr/bin/env python
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you find **at least two datasets** on the web which are related, and that you visualize these datasets to answer the assignment question. You are free to utilize datasets with any location or domain, the usage of **Ann Arbor sports and athletics** datasets in the example is just a suggestion.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * You must state a question you are seeking to answer with your visualizations.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together as an example! [Example Solution File](./readonly/Assignment4_example.pdf)

# # 1 Region and Domain
# 
# State the region and the domain category that your data sets are about
# 
#     Ann Arbor, Michigan, United States
#     Sports and Athletics
# 
# # 2 Research Question
# 
# You must state a question about the domain category and region that you identified as being interesting
# 
#     How have the win percentages for the four major Detroit sports teams (The Detroit Pistons, The Red
#     Wings, The Detroit Tigers, and The Detroit Lions) change over the last forty years?
# 
# # 3 Links
# 
# You must provide at least two links to publicly accessible datasets. These could be links to
# files such as CSV or Excel files, or links to websites which might have data in tabular form,
# such as Wikipedia pages.
# 
# - https://en.wikipedia.org/wiki/List_of_Detroit_Pistons_seasons
# - https://en.wikipedia.org/wiki/List_of_Detroit_Red_Wings_seasons
# - https://en.wikipedia.org/wiki/List_of_Detroit_Tigers_seasons
# - https://en.wikipedia.org/wiki/List_of_Detroit_Lions_seasons

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import matplotlib.colors as col
import matplotlib.cm as cm
import seaborn as sns
import re

# %matplotlib notebook

plt.style.use('seaborn-v0_8-colorblind')


# In[2]:


dict_datasets={
    "Tigers":"view-source_https___en.wikipedia.org_wiki_List_of_Detroit_Tigers_seasons.html",
    "Lions":"view-source_https___en.wikipedia.org_wiki_List_of_Detroit_Lions_seasons#Seasons.html",
    "Pistons":"view-source_https___en.wikipedia.org_wiki_List_of_Detroit_Pistons_seasons.html",
    "RedWings":"view-source_https___en.wikipedia.org_wiki_List_of_Detroit_Red_Wings_seasons.html",
}


# In[3]:


df_lions=pd.read_html(dict_datasets['Lions'])[1][6:95]


# In[4]:


df_lions.head()


# In[5]:


df_lions['Season']['Season']


# In[6]:


lions=pd.DataFrame()
lions['Year']=df_lions['Season']['Season']


# In[7]:


df_lions.rename(columns = {'.mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}W': 'W'}, inplace=True)


# In[8]:


lions['Wins']=df_lions['Regular season']['W'].astype(int)


# In[9]:


lions['Losses']=df_lions['Regular season']['L'].astype(int)


# In[10]:


lions['Win %_Lions']=lions['Wins']/(lions['Wins']+lions['Losses'])


# In[11]:


lions


# In[12]:


df_pistons=pd.read_html(dict_datasets['Pistons'])[1][11:]


# In[13]:


df_pistons.rename(columns = {'.mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}Season': 'Season'}, inplace=True)


# In[14]:


df_pistons.head()


# In[15]:


pistons=pd.DataFrame()
pistons['Year']=df_pistons['Season'].str[:4]
pistons[['Wins','Losses']]=df_pistons[['Wins','Losses']]
pistons['Wins'] = pd.to_numeric(pistons['Wins'], errors='coerce')
pistons['Losses'] = pd.to_numeric(pistons['Losses'], errors='coerce')

pistons['Win %_Pistons']=pistons['Wins']/(pistons['Wins']+pistons['Losses'])


# In[16]:


pistons


# In[17]:


df_tigers=pd.read_html(dict_datasets['Tigers'])[1]


# In[18]:


df_tigers


# In[19]:


tigers=pd.DataFrame()


# In[20]:


tigers[['Year','Wins','Losses']]=df_tigers[['Season','Wins','Losses']].copy()


# In[21]:


tigers['Year']=tigers['Year'].astype(str)
tigers['Year']=tigers['Year'].astype(object)
tigers['Wins'] = pd.to_numeric(tigers['Wins'], errors='coerce')
tigers['Losses'] = pd.to_numeric(tigers['Losses'], errors='coerce')


# In[22]:


tigers['Win %_Tigers']=tigers['Wins']/(tigers['Wins']+tigers['Losses'])


# In[23]:


tigers = tigers[tigers['Year'] != "Totals"]


# In[24]:


tigers


# In[25]:


df_redw=pd.read_html(dict_datasets['RedWings'])[2][1:100]


# In[26]:


df_redw.rename(columns = {'Regular season[3][6][7][8]': 'Regular season'}, inplace=True)


# In[27]:


redw=pd.DataFrame()
redw['Year']=df_redw['NHL season']['NHL season'].str[:4]
redw[['Wins','Losses']]=df_redw['Regular season'][['W','L']]
redw=redw.set_index('Year')


# In[28]:


redw


# In[29]:


# missing 2004
redw.loc['2004',['Wins','Losses']]=redw.loc['2003'][['Wins','Losses']]

redw['Wins'] = pd.to_numeric(redw['Wins'], errors='coerce')
redw['Losses'] = pd.to_numeric(redw['Losses'], errors='coerce')

redw['Win %_RedWings']=redw['Wins']/(redw['Wins']+redw['Losses'])
redw=redw.reset_index() 


# In[30]:


redw = redw[redw['Year'] != 'Detr']
redw.reset_index(drop=True, inplace=True)


# In[31]:


redw


# In[32]:


# Merge data for visualize
Big4_Michigan=pd.merge(lions.drop(['Wins','Losses'], axis=1),tigers.drop(['Wins','Losses'], axis=1),on='Year')
Big4_Michigan=pd.merge(Big4_Michigan,pistons.drop(['Wins','Losses'], axis=1),on='Year')
Big4_Michigan=pd.merge(Big4_Michigan,redw.drop(['Wins','Losses'], axis=1),on='Year')


# In[33]:


Big4_Michigan


# In[34]:


Big4_Michigan[40:]


# In[35]:


# %matplotlib notebook
# Draw KDE
kde=Big4_Michigan.plot.kde()
[kde.spines[loc].set_visible(False) for loc in ['top', 'right']]
kde.axis([0,1,0,6])
kde.set_title('KDE of Big4 Win % in Michigan\n(1950-2022)',alpha=0.8)
kde.legend(['Lions','Tigers','Pistons','Red Wings'],loc = 'best',frameon=False, title='Big4', fontsize=10)


# In[37]:


get_ipython().run_line_magic('matplotlib', 'notebook')

Big4_Michigan_0019=Big4_Michigan[40:]
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)
axs=[ax1,ax2,ax3,ax4]

fig.suptitle('Big4 Win % in Michigan\n(1982-2022)',alpha=0.8);

# Properties
columns_w=['Win %_Lions','Win %_Tigers','Win %_Pistons','Win %_RedWings']
colors=['g','b','y','r']
titles=['NFL: Lions','MLB: Tigers','NBA: Pistons','NHL: Red Wings']
axis=[0,20,0,0.8]

y=0.5

for i in range(len(axs)):
    
    ax=axs[i]
    
    ax = sns.pointplot(x=Big4_Michigan_0019['Year'], y=Big4_Michigan_0019[columns_w[i]], scale=0.7, ax=ax)
    ax.axhline(y=0.5, color='gray', linewidth=1, linestyle='--')
    ax.fill_between(range(len(Big4_Michigan_0019)), 0.5, Big4_Michigan_0019[columns_w[i]], where=(Big4_Michigan_0019[columns_w[i]] < y), color='red', interpolate=True, alpha=0.3)
    ax.fill_between(range(len(Big4_Michigan_0019)), 0.5, Big4_Michigan_0019[columns_w[i]], where=(Big4_Michigan_0019[columns_w[i]] > y), color='blue', interpolate=True, alpha=0.3)
    
    # Beautify the plot
    [ax.spines[loc].set_visible(False) for loc in ['top', 'right']] # Turn off some plot rectangle spines
    ax.set_ylabel('Win % ', alpha=0.8)
    ax.set_xlabel('Year', alpha=0.8)
    ax.set_title(titles[i], fontsize=10, alpha=0.8)
    ax.axis(axis)
    ax.set_xticks(np.append(np.arange(0, 20, 5),19)) 
    ax.set_xticklabels(['1982','1992','2002','2012','2022'], fontsize=8, alpha=0.8)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(8)
        label.set_bbox(dict(facecolor='white',edgecolor='white',  alpha=0.8))

plt.show()


# In[ ]:





# In[ ]:




