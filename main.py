from rb import *
import time
from sklearn.metrics import classification_report
# -------------------------------------- Carrega os dados
database = "./databases/car.features"
read_data(database)

arq = open(database, 'r')
data = arq.readlines()
arq.close()

# ------------------------------------------------ Inicia Calculos
mat_confusao = [[0 for i in range(4)] for j in range(4)]
predicoes = []
original = []

print("Calculando dados via Redes Bayesianas...\n")

tempo = time.time()
for amos in data:
    aux = amos.split(',')

    feat = {"buying":aux[0],
            "maint":aux[1],
            "doors":aux[2],
            "persons":aux[3],
            "lug_boot":aux[4],
            "safety":aux[5]
            }
    pred, prob = predict_bay_net(feat)

    # para indexar a matrix de confusao
    i = tags[aux[6][:-1]] # classe real
    j = tags[pred] # predicao

    mat_confusao[i][j] += 1

    original.append(i)
    predicoes.append(j)

print(mat_confusao)

count = 0
for i in range(4):
    count += mat_confusao[i][i]

print("Acuracia = {0}/{1} = {2} | Execucao: {3}s".format(count, 1728, count/1728*100, time.time() - tempo))

print(classification_report(original, predicoes))