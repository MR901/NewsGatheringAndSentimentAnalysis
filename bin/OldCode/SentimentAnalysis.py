# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import re


# In[2]:


data = pd.read_csv("/home/shieldsqaure/Downloads/Sentiment.csv")


# In[6]:


data


# In[3]:


data = data[['text','sentiment']]


# In[4]:


data['text'] = data['text'].apply(lambda x: x.lower())
data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))


# In[5]:


for idx,row in data.iterrows():
    row[0] = row[0].replace('rt',' ')


# In[6]:


max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')


# In[7]:


tokenizer.fit_on_texts(data['text'].values)


# In[8]:


X = tokenizer.texts_to_sequences(data['text'].values)


# In[9]:


X = pad_sequences(X)


# In[10]:


X.shape


# In[11]:


embed_dim = 128
lstm_out = 196

model = Sequential()
model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(3,activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())


# In[12]:


Y = pd.get_dummies(data['sentiment']).values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.33, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)


# In[13]:


batch_size = 32
model.fit(X_train, Y_train, epochs = 10, batch_size=batch_size, verbose = 2)


# In[15]:


model.predict("aman  cool")


# In[16]:


validation_size = 1500

X_validate = X_test[-validation_size:]
Y_validate = Y_test[-validation_size:]
X_test = X_test[:-validation_size]
Y_test = Y_test[:-validation_size]
score,acc = model.evaluate(X_test, Y_test, verbose = 2, batch_size = batch_size)
print("score: %.2f" % (score))
print("acc: %.2f" % (acc))


# In[21]:


def test_sentiment(twt):
    twt = tokenizer.texts_to_sequences(twt)
#padding the tweet to have exactly the same shape as `embedding_2` input
    twt = pad_sequences(twt, maxlen=28, dtype='int32', value=0)
#     print(twt)
    sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]
    if(np.argmax(sentiment) == 0):
        print("negative")
    elif (np.argmax(sentiment) == 1):
        print("positive")
# 0 means negative 
# 1 means positive
# 2 means neutral


# In[24]:


test_sentiment("Airtel board sets up panel to explore fund raising options for strengthening balance sheet")


# In[123]:


data_test = pd.read_csv("/home/shieldsqaure/Downloads/news_sample.csv")


# In[124]:


data_test_cut = data_test[["headline","sentimentNegative","sentimentNeutral","sentimentPositive"]]


# In[125]:


sent = list()
for i in data_test.index:
    sent.append(test_sentiment(data_test_cut["headline"][i]))


# In[126]:


data_test_cut["headline"] = data_test_cut["headline"].apply(lambda x : x.lower())


# In[106]:


data_prize = pd.read_csv("/home/shieldsqaure/Downloads/marketdata_sample.csv")


# In[117]:


data_prize.drop(columns=["returnsOpenPrevMktres1","returnsClosePrevMktres1"],axis =1,inplace=True)


# In[119]:


data_prize["universe"].unique()


# In[121]:


data_prize.columns


# In[129]:


# import lightgbm as lgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import chain

get_ipython().magic(u'matplotlib inline')


# In[163]:


