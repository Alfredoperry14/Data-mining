"""
Cluster the following data into k = 2 clusters using the k-medoids algorithm
with Manhattan distance.

Points:
(2,6), (3,4), (3,8), (4,7), (6,2), (7,3)

Initial medoids:
M1 = (3,8), M2 = (4,7)
"""

import numpy as np

x1 = np.array([2, 3, 3, 4, 6, 7])
x2 = np.array([6, 4, 8, 7, 2, 3])

data = np.column_stack((x1, x2))

# Starting medoids
medoids = [np.array([3, 8]), np.array([4, 7])]

# Manhattan distance
def manhattan_distance(points, medoid):
    return np.sum(np.abs(points - medoid), axis=1)

for iteration in range(10):
    #m1 and m2 are arrays of the distance from the points to each medoid
    m1 = manhattan_distance(data, medoids[0])
    m2 = manhattan_distance(data, medoids[1])

    bin1, bin2 = [], []

    # Compare distances to both medoids for each data point
    for i in range(len(data)):
        distances = [m1[i], m2[i]]

        min_source = np.argmin(distances)
        min_value = distances[min_source]

        if min_source == 0:
            bin1.append(data[i])
        elif min_source == 1:
            bin2.append(data[i])

        print(f"Index {i}: min = {min_value} from {min_source}")

    # Convert bins to arrays
    bin1 = np.array(bin1)
    bin2 = np.array(bin2)

    # Update medoids:
    # choose the point in each cluster with the smallest total Manhattan distance
    new_medoids = []

    for cluster_index, cluster in enumerate([bin1, bin2]):

        #If all the points were at one medoid
        if len(cluster) == 0:
            new_medoids.append(medoids[cluster_index])
            continue

        best_point = None
        best_cost = float("inf")

        #Try each point as a possible medoid
        for candidate in cluster:
            #Manhattan distance of candidate to every other point in the cluster
            cost = np.sum(np.sum(np.abs(cluster - candidate), axis=1))

            if cost < best_cost:
                best_cost = cost
                best_point = candidate

        new_medoids.append(best_point)

    # Stop if medoids do not change
    if np.array_equal(new_medoids[0], medoids[0]) and np.array_equal(new_medoids[1], medoids[1]):
        print(f"\niter {iteration}")
        print("bins:", bin1.tolist(), bin2.tolist())
        print("medoids:", medoids, "->", new_medoids)
        break

    print(f"\niter {iteration}")
    print("bins:", bin1.tolist(), bin2.tolist())
    print("medoids:", medoids, "->", new_medoids)

    medoids = new_medoids
    # End of loop

print("\nFinal medoids:")
print(medoids)

print("\nFinal bins:")
print("bin1:", bin1)
print("bin2:", bin2)