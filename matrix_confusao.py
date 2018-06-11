#-*- coding: utf-8 -*-
import csv

from sklearn.metrics import confusion_matrix, cohen_kappa_score

n_linhas = 19
n_colunas = 2000
dataset = [[9]*n_colunas for _ in range(n_linhas)]
print dataset
with open('planilhas/nomePlanilha.csv', 'rb') as csvfile:
    linhas = csv.reader(csvfile, delimiter=';', quotechar='|')
    num_lin = 0
    for l in linhas:
        for col in range(0, n_linhas):
            # print  str(num_lin) + ' ' + str(i) + ' ' + l[i]
            print str(col) + ' ' + str(num_lin) + ' = ' + str(l[col])
            dataset[col][num_lin] = int(l[col])
        num_lin += 1
    print dataset

y_true = dataset[0]

for i in range(1, n_linhas):
    print '--------'
    y_pred = dataset[i]
    print y_true
    print y_pred

    matrix_confusao = confusion_matrix(y_true, y_pred, labels=[1, 0, -1])
    print matrix_confusao

    #para ser considerado concordancia quase perfeita deve ser >= 0,8
    kappa = cohen_kappa_score(y_true, y_pred, labels=[1, 0, -1])
    print kappa