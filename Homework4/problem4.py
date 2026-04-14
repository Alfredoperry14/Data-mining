import numpy as np
blue_class = [(0.5, 1), (1, 3), (2,1)]
red_class = [(3,3), (3,6), (4, 5.75), (5, 4)]


def distance(p1, p2):
    return np.sqrt(np.square(p1[0] - p2[0]) + np.square(p1[1] - p2[1]))

min_dist = float("inf")
max_dist = float("-inf")
for blue in blue_class:
    for red in red_class:
        dist = distance(blue, red)
        min_dist = min(dist, min_dist)
        max_dist = max(dist, max_dist)
print(min_dist)
print(max_dist)