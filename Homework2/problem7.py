from matplotlib import pyplot as plt
import pandas as pd
#Df stands for data frame
df = pd.read_csv("Iris_Flower_Dataset_.csv")

print(len(df))

colors = {
    "Iris-setosa": "red",
    "Iris-versicolor": "orange",
    "Iris-virginica": "blue"
}

markers = {
    "Iris-setosa": "o",   # Circle
    "Iris-versicolor": "s",  # Square
    "Iris-virginica": "d"    # Triangle
}

#Get every distinct species
iris_species = df["species"].unique()

#For each species
for species in iris_species:
    subset = df[df["species"] == species]
    plt.scatter(subset["sepal_length"],
                subset["sepal_width"],
                color=colors[species],
                marker=markers[species],
                label=species)

plt.title("Petal length vs Petal width")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.legend()
plt.show()



