"""
4) Suppose a group of 12 sales price records has been sorted as follows: 5, 10, 11, 13, 15, 35, 50,
55, 72, 92, 204, 215. Partition them into 3 bins by each of the following methods:
c) Clustering.
"""
#I am going to do K means clustering on this data set
import numpy as np
from matplotlib.cbook import index_of

data = np.array([5,10,11,13,15,35,50,55,72,92,204,215])
#Choosing 3 starting centroids randomly
centroids = [11, 50, 92]

#for each m calculate an array based on x-m
#sqrt((centroid - newdata)^2)
#Find min data for every data point

for iteration in range(10):
    m1 = np.sqrt(np.square(centroids[0]- data))
    m2 = np.sqrt(np.square(centroids[1]- data))
    m3 = np.sqrt(np.square(centroids[2]- data))

    bin1, bin2, bin3 = [], [], []
    #Compare all ms at the same index to find the mins
    for i in range(len(data)):
        values = {
            'm1': m1[i],
            'm2': m2[i],
            'm3': m3[i]
        }
        min_source = min(values, key=values.get)
        min_value = values[min_source]

        if min_source == 'm1':
            bin1.append(data[i])
        elif min_source == 'm2':
            bin2.append(data[i])
        elif min_source == 'm3':
            bin3.append(data[i])

        print(f"Index {i}: min = {min_value} from {min_source}")

    new_centroids = [
        np.mean(bin1) if len(bin1) else centroids[0],
        np.mean(bin2) if len(bin2) else centroids[1],
        np.mean(bin3) if len(bin3) else centroids[2],
    ]
    #If they're close enough
    if np.allclose(new_centroids, centroids, 0.05):
        break
    print(f"\niter {iteration}")
    print("bins:", bin1, bin2, bin3)
    print("centroids:", centroids, "->", new_centroids)
    old_centroids = centroids
    centroids = new_centroids
    #End of Loop

print("Final bins:",
      list(map(int, bin1)),
      list(map(int, bin2)),
      list(map(int, bin3)))