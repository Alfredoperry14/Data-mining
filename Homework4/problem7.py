"""
6.7 Develop a computer program to implement a k-means clustering algorithm in a computer
language such as C++ or Matlab. Then use the program to classify the following data assuming k
= 3
"""
#I am going to do K means clustering on this data set
import numpy as np

a1 = np.array([21, 20, 20, 17, 31, 1, 24, 29, 60, 83, 73, 85, 81, 63, 57, 69, 67, 62, 15, 28, 31, 33, 44, 26, 36, 38, 39])
a2 = np.array([40, 38, 31, 39, 38, 26, 25, 26, 45, 55, 35, 32, 38, 47, 31, 28, 39, 39, 52, 62, 62, 52, 54, 69, 59, 63, 61])

data = np.column_stack((a1, a2))

#Choosing 3 starting centroids randomly
centroids = [(20,38), (15,52), (39, 61)]

# Subtract centroid from all data points
# Square the differences → (dx^2, dy^2)
# Sum across each point(x,y) → dx^2 + dy^2
# Then take square root → Euclidean distance

for iteration in range(10):
    m1 = np.sqrt(np.sum((data - centroids[0]) ** 2, axis=1))
    m2 = np.sqrt(np.sum((data - centroids[1]) ** 2, axis=1))
    m3 = np.sqrt(np.sum((data - centroids[2]) ** 2, axis=1))


    bin1, bin2, bin3 = [], [], []

    #Compare all ms at the same index to find the mins
    for i in range(len(data)):
        distances = [m1[i], m2[i], m3[i]]

        min_source = np.argmin(distances)

        min_value = distances[min_source]

        if min_source == 0:
            bin1.append(data[i])
        elif min_source == 1:
            bin2.append(data[i])
        elif min_source == 2:
            bin3.append(data[i])

        print(f"Index {i}: min = {min_value} from {min_source}")

    new_centroids = [
        np.mean(bin1, axis=0) if len(bin1) else centroids[0],
        np.mean(bin2, axis=0) if len(bin2) else centroids[1],
        np.mean(bin3, axis=0) if len(bin3) else centroids[2],
    ]
    #If they're within .05
    if np.allclose(new_centroids, centroids, 0.05):
        break
    print(f"\niter {iteration}")
    print("bins:", bin1, bin2, bin3)
    print("centroids:", centroids, "->", new_centroids)
    old_centroids = centroids
    centroids = new_centroids
    #End of Loop

print("\nFinal centroids:")
print(centroids)

print("\nFinal bins:")
print("bin1:", bin1)
print("bin2:", bin2)
print("bin3:", bin3)


import matplotlib.pyplot as plt

# Convert bins to arrays
bin1 = np.array(bin1)
bin2 = np.array(bin2)
bin3 = np.array(bin3)

centroids = np.array(centroids)

plt.figure(figsize=(6,6))

# Plot each cluster with a different color
plt.scatter(bin1[:,0], bin1[:,1], label='Cluster 1')
plt.scatter(bin2[:,0], bin2[:,1], label='Cluster 2')
plt.scatter(bin3[:,0], bin3[:,1], label='Cluster 3')

# Plot centroids (bigger + different marker)
plt.scatter(centroids[:,0], centroids[:,1],
            marker='X', s=200, label='Centroids')

plt.xlabel('a1')
plt.ylabel('a2')
plt.title('K-means Clustering (k=3)')
plt.legend()
plt.grid()

plt.show()