# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#Conexão mongodb
from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
banco = cliente.sams
tweets_collection = banco.tweets
erros_collection = banco.erros


for t in tweets_collection.find():

    stopWords = set(stopwords.words('english'))
    words = word_tokenize(t['tweet'])
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    print(wordsFiltered)