#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import ast 
from collections import Counter
from wordcloud import WordCloud


# In[ ]:





# In[2]:


movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')


# In[3]:


movies.head(3)


# In[4]:


credits.head()


# In[5]:


print("Shape of movies dataset:",movies.shape)
print("Shape of credits dataset:",credits.shape)


# In[6]:


movies.info()


# In[7]:


credits.info()


# In[8]:


# Joining the two datsets
movies = pd.merge(left = movies, right = credits, on='title')


# In[9]:


movies = movies.drop(columns=['homepage','tagline','id','overview','status','original_title','movie_id'])


# In[10]:


movies.head(3)


# In[11]:


movies['genres'][0]


# In[12]:


# Tidying up genre, production_companies and production_countries column
def func(obj):
    List = []
    for i in ast.literal_eval(obj):
        List.append(i['name'])
    return List


# In[13]:


movies['genres'] = movies['genres'].apply(func)
movies['genres'][0]


# In[14]:


movies['production_companies'] = movies['production_companies'].apply(func)
movies['production_countries'] = movies['production_countries'].apply(func)
movies.head(3)


# In[15]:


genres = Counter()
for i in range(movies.shape[0]):
    for j in movies.genres[i]:
        genres[j]+=1
Genres = pd.DataFrame.from_dict(genres, orient='index').reset_index()
Genres = Genres.rename(columns = {'index': 'Genres' ,0: 'Frequency'})
Genres.loc[Genres['Frequency'] < 200, 'Genres'] = 'Others'


# # Q1: Use bar chart to draw genres of movies.

# In[16]:


fig = px.bar(Genres, x="Frequency", y="Genres", color="Genres", title="Genres of movies")
fig.show()


# # Q2: Use pie chart to draw top 5 languages.

# In[17]:


# Top Production Counties
prod_cont = Counter()
for i in range(movies.shape[0]):
    for j in movies.production_countries[i]:
        prod_cont[j]+=1
movie_prod_cont = pd.DataFrame.from_dict(prod_cont, orient='index').reset_index()
movie_prod_cont = movie_prod_cont.rename(columns = {'index': 'Production Country' ,0: 'Frequency'})
movie_prod_cont=movie_prod_cont.sort_values(by = ['Frequency'],ascending=False).reset_index().head(5)
movie_prod_cont


# In[18]:


fig = px.pie(movie_prod_cont, values='Frequency', names='Production Country', title='top 5 languages')
fig.show()


# # Q3: Use WordCloud to draw genres.

# In[19]:


Genres


# In[20]:


plt.subplots(figsize = (8,8))

wordCloud = WordCloud (
                    background_color = 'white',
                     width = 512,
                     height = 384
                            ).generate(' '.join(Genres.Genres))
plt.imshow(wordCloud)
plt.axis('off')
# plt.savefig('Plotly-World_Cloud.png')


# # Q4: Use scatter to draw the relationship between budget and revenue.

# In[21]:


fig = px.scatter(x=['budget'], y=['revenue'])
fig.show()


# # Q5: Use line chart to draw the relationship between revenue and popularity.

# In[22]:


fig = px.line(movies, x="revenue", y="popularity", title='the relationship between revenue and popularity')
fig.show()


# # Q6: Draw an extra chart from your choice.

# In[52]:





# In[ ]:





# In[ ]:




