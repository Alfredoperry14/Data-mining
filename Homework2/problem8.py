import math
import sys
from statistics import covariance

import pandas as pd

#Df stands for data frame
df = pd.read_csv("Iris_Flower_Dataset_.csv")

#print(len(df))

#Min euclidean distance must be positive
# -1 can be the min
# sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
#"Iris-setosa","Iris-versicolor", Iris-virginica
#i.) setosa vs virginica, ii.) setosa vs versi, iii.) versi vs virginica

#species = ["Iris-setosa", "Iris-virginica", "Iris-versicolor"]

setosa = df[df["species"] == "Iris-setosa"]
virginica = df[df["species"] == "Iris-virginica"]
versicolor = df[df["species"] == "Iris-versicolor"]

setosa_petal = setosa[["petal_length", "petal_width"]]
virginica_petal = virginica[["petal_length", "petal_width"]]
versicolor_petal = versicolor[["petal_length", "petal_width"]]

#i.) setosa vs virginica
#Two find the closest points I can find

def distance(s, v):
    return math.sqrt((s[0] - v[0])**2 + (s[1] - v[1])**2)

minDistance = sys.maxsize
for s in setosa_petal.itertuples(index=False):
    for vir in virginica_petal.itertuples(index=False):
        minDistance = min(minDistance,distance(s,vir))
#ii
print('Min Distance between setosa and virginica', minDistance)

minDistance = sys.maxsize
for s in setosa_petal.itertuples(index=False):
    for vir in versicolor_petal.itertuples(index=False):
        minDistance = min(minDistance,distance(s,vir))
#iii
print('Min Distance between setosa and versicolor', minDistance)

minDistance = sys.maxsize
for s in setosa_petal.itertuples(index=False):
    for vir in virginica_petal.itertuples(index=False):
        minDistance = min(minDistance,distance(s,vir))

print('Min Distance between versicolor and virginica', minDistance)

#Sxy -> Covariance
#Sx, Sy -> Standard deviation
#Part C finding average correlation between two points (Petal length vs petal width)
petal_width = df["petal_width"]
petal_length = df["petal_length"]

petal_width_mean = petal_width.mean()
petal_length_mean = petal_length.mean()

#Covariance
covariance_pw = petal_width - petal_width_mean
covariance_pl = petal_length - petal_length_mean

covariance = (covariance_pl * covariance_pw).sum() / (len(petal_length) - 1)
print('Covariance between petal width and petal length', covariance)

std_pw = ((petal_width - petal_width_mean) ** 2).sum() / (len(petal_width) - 1)
std_pw = math.sqrt(std_pw)

std_pl = ((petal_length - petal_length_mean) ** 2).sum() / (len(petal_length) - 1)
std_pl = math.sqrt(std_pl)
print('Standard deviation of petal width and petal length', std_pl)

correlation = covariance / (std_pl * std_pw)
print('Correlation between petal width and petal length', correlation)

#Part D
#Figure 3
pl = 2.6

def figure3(petal_length):
    print("Figure 3", end=": ")
    if pl <= 2.5:
        print("Setosa")
    elif pl <= 4.75:
        print("Versicolor")
    else:
        print("Virginica")

def figure4(petal_length):
    print("Figure 4", end=": ")
    if pl > 2.45 and pl > 5.05:
        print("Virginica")
    elif petal_length > 2.45 and petal_length <= 5.05:
        print("Versicolor")
    else:
        print("Setosa")


figure3(pl)
figure4(pl)
#The answer for part D is Versicolor