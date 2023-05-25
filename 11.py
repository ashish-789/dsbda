#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install textblob


# In[5]:


from textblob import TextBlob
Feedback1 = "The Food at Radison was awesome"
Feedback2 = "The Food at Radison was very good"
blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
print(blob1.sentiment)
print(blob2.sentiment)


# In[6]:


pip install wordcloud


# In[7]:


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


# In[8]:


df = pd.read_csv("D:/New folder (3)/Youtube04-Eminem.csv")


# In[9]:


comment_words = ''
stopwords = set(STOPWORDS)


# In[11]:


for val in df.CONTENT:
# typecaste each val to string
        val = str(val)
# split the value
        tokens = val.split()
        for i in range(len(tokens)):
                 tokens[i] = tokens[i].lower()
        comment_words += " ".join(tokens)+" "
wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='white',
                        stopwords = stopwords,
                        min_font_size = 10).generate(comment_words)


# In[12]:


plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()


# In[13]:


pip install textblob


# In[14]:


from textblob import TextBlob
Feedback1 = "The Food at Radison was awesome"
Feedback2 = "The Food at Radison was very good"
blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
print(blob1.sentiment)
print(blob2.sentiment)


# In[15]:


pip install wordcloud


# In[16]:


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


# In[18]:


df = pd.read_csv("D:/New folder (3)/Youtube04-Eminem.csv")


# In[19]:


comment_words = ''
stopwords = set(STOPWORDS)


# In[20]:


for val in df.CONTENT:
# typecaste each val to string
        val = str(val)
# split the value
        tokens = val.split()
        for i in range(len(tokens)):
                 tokens[i] = tokens[i].lower()
        comment_words += " ".join(tokens)+" "
wordcloud = WordCloud(width = 800, height = 800,background_color ='white',stopwords = stopwords,min_font_size = 10).generate(comment_words)


# In[21]:


plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()


# In[ ]:





# In[ ]:




