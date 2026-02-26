import math

from matplotlib import pyplot as plt
import pandas as pd
#Df stands for data frame
df = pd.read_csv("Iris_Flower_Dataset_.csv")

print(len(df))

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

def demo(**kwargs):
    print("kwargs:", kwargs)

#def distance(**kwargs):
    #return math.sqrt((s[0] - v[0])**2 + (s[1] - v[1])**2)

for petal in setosa_petal.itertuples(index=False):
    print(demo(petal))

