# -*- coding: utf-8 -*-
import csv
from pymongo import MongoClient
from sklearn import cross_validation

# Analisa a frequencia das palavras e o somatório de acertos de cada método (Rotulados Humano x Classificados Máquina).

#Conexão mongodb
cliente = MongoClient('localhost', 27017)
banco = cliente.sams
tweets_collection = banco.tweets
erros_collection = banco.erros

wordstring = ''

# A ordem dos algoritmos deve ser a mesma do dataset CSV.
algoritmos = ['OPINIONLEXICON', 'SENTISTRENGTH', 'SOCAL', 'HAPPINESSINDEX', 'SANN', 'EMOTICONSDS', 'SENTIMENT140', 'STANFORD', 'AFINN', 'MPQA', 'NRCHASHTAG', 'EMOLEX', 'EMOTICONS', 'PANAST', 'SASA', 'SENTIWORDNET', 'VADER', 'UMIGON']

acertos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
with open('planilhas/teste-pati.csv', 'rb') as csvfile:
    tweets = csv.reader(csvfile, delimiter=';', quotechar='|')
    for tweet in tweets:
        if tweet[1] == '-1':
            tweet[1] = 'Negative'
        elif tweet[1] == '0':
            tweet[1] = 'Neutral'
        elif tweet[1] == '1':
            tweet[1] = 'Positive'
        # print tweet[0] + ': ' + str(len(tweet))
        wordstring += tweet[0]
        for i in range(2, len(tweet)):
#         print tweet[1] + ' = ' + tweet[i]
            if tweet[1] == tweet[i]:
                acertos[i-2] += 1

#ordenação
acertos, algoritmos = zip(*sorted(zip(acertos, algoritmos)))

for i in range(0, len(acertos)):
    print algoritmos[i] + ': ' + str(acertos[i])

#contagem das palavras
wordlist = wordstring.split()
wordfreq = []


for w in wordlist:
    wordfreq.append(wordlist.count(w))
    pares = zip(wordlist, wordfreq)


for p in pares:
    print p


from sklearn import cross_validation



def stratified_cv(X, y, clf_class, shuffle=True, n_folds=10, **kwargs):

    stratified_k_fold = cross_validation.StratifiedKFold(y, n_folds=n_folds, shuffle=shuffle, random_state=12)
    y_pred = y.copy()

    for ii, jj in stratified_k_fold:
        X_train, X_test = tweet[1], tweet[jj]
        y_train = tweet[1]
        clf = clf_class(**kwargs)
        clf.fit(X_train,y_train)
        y_pred[jj] = clf.predict(X_test)
    return y_pred
