import numpy as np
P = [0.49, 0.105, 0.105, 1.05, 1.05, 0.0225, 0.0225, 0.0225, 0.0225]
print(P.count())


ans = 0
for prob in P:
    ans += prob * np.log2(prob)
    print("Entropy at S,", P.index(prob), "is", ans)
ans = -ans