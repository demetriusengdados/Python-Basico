#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark.mllib.feature import WordVec2


# In[ ]:


input = sc.textfile("text_by_line").map(lambda row: row.split(" "))


# In[ ]:


word2Vec = Word2Vec()
model = wprd2vec.fit(input)


# In[ ]:


synonyms = model.findSynonyms('china', 40)


# In[ ]:


for word, cosine_distance in synonyms:
    print("{}: {}".format(word, cosine_distance))


# In[ ]:




