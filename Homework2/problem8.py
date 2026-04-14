import math
import sys
import pandas as pd

#Df stands for data frame
df = pd.read_csv("Iris_Flower_Dataset_.csv")
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

def distance(s, v):
    return math.sqrt((s[0] - v[0])**2 + (s[1] - v[1])**2)
#i.) setosa vs virginica
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
attributes = {
"sepal_length" : df["sepal_length"],
"sepal_width" : df["sepal_width"],
"petal_length" : df["petal_length"],
"petal_width" : df["petal_width"],
}

def correlation(x, y):
    x_mean = x.mean()
    y_mean = y.mean()

    x_cov = x - x_mean
    y_cov = y - y_mean

    covariance = (x_cov * y_cov).sum() / (len(x) - 1)

    std_x = ((x - x_mean) ** 2).sum() / (len(x) - 1)
    std_x = math.sqrt(std_x)

    std_y = ((y - y_mean) ** 2).sum() / (len(y) - 1)
    std_y = math.sqrt(std_y)

    correlation = covariance / (std_x * std_y)
    return correlation

for x_name in attributes:
    for y_name in attributes:
        print(x_name, "vs", y_name, "=",
              round(correlation(attributes[x_name], attributes[y_name]), 4))
    print()
#Comparing the pandas table compared to the manual one shows they're the same
print("Pandas Function:")
print(df.corr(numeric_only=True))

#Part D
#Did the rule model for Figure 3 & 4
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

