import pandas as pd
import numpy as np
import html 
import re
import warnings 
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer #for vectorize text into sparse matrix 
from sklearn.feature_extraction.text import TfidfVectorizer

class cleasing():
    def __init__(self, Data, token = None):
        self.Data = Data
        self.token = token

    def cleansingData(self):
        NewsData = self.Data.drop(columns=['sumber', 'link','created_at'])
        NewsData['content'] = NewsData['content'].str.lower()
        # untuk menghapus apapun selain text 
        NewsData['content']=NewsData['content'].str.replace("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([0-9])","")
        #step tokenize
        NewsData['content'] = NewsData['content'].apply(nltk.word_tokenize)
        #Mengapus Stopword
        data = pd.read_csv("C:\\Users\\eBdesk\\Documents\\Untitled Folder\\indonesian_stopword.txt")
        data['\'\'']
        NewsData['content'] = NewsData['content'].apply(lambda x: [y for y in x if y not in data['\'\''].tolist()])
        NewsData['content'] = NewsData['content'].str.join(" ")
        #tfidf untuk no stemming
        if(self.token is None):
            vectorizer2 = TfidfVectorizer(stop_words = None, tokenizer = None)
            tfidf_wm = vectorizer2.fit_transform(NewsData['content'])
            word_features2 = vectorizer2.get_feature_names()
            return pd.DataFrame(tfidf_wm.toarray(), columns=vectorizer2.get_feature_names())
        elif(self.token == "true"):
            list1 = []
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()
            stm_tfidf=NewsData
            for index,row in NewsData.iterrows():
                res= stemmer.stem(row['content'])
                list1.append(res)
            stm_tfidf['content']=list1
            vectorizer2 = TfidfVectorizer(stop_words = None, tokenizer = None)
            tfidf_wm = vectorizer2.fit_transform(stm_tfidf['content'])
            word_features2 = vectorizer2.get_feature_names()
            return pd.DataFrame(tfidf_wm.toarray(), columns=vectorizer2.get_feature_names())
        else :
            return None