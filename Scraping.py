
# coding: utf-8

# In[52]:


import requests
k= requests.get('http://mentalfloss.com/article/63666/50-facts-about-star-wars')


# In[53]:


print (k.text[:400])


# In[54]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(k.text, 'html.parser')


# In[55]:


facts = soup.find_all('h4')


# In[56]:


len(facts)


# In[57]:


facts[0].text


# In[58]:


table = []
for i in facts[:50]:
    fact = i.text
    table.append(fact)


# In[59]:


len(table)


# In[60]:


table[:5]


# In[62]:


table


# In[64]:


import pandas as pd
df = pd.DataFrame(table, columns=['list'])


# In[65]:


df.head()


# In[67]:


df.to_csv('star_facts.csv', index=False, encoding='utf-8')


# In[69]:


df = pd.read_csv('star_facts.csv', encoding='utf-8')


# In[70]:


df.head(7)

