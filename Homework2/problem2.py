#Problem 2
import numpy as np
P = [0.49, 0.105, 0.105, 0.105, 0.105, 0.0225, 0.0225, 0.0225, 0.0225]
print(len(P), 'probabilities')
print('The sum of all of the probabilities was', np.sum(P))
ans = 0
#print("Entropy is the negative of the total sum of each probability multiplied by log2(probability)")
for probIndex, prob in enumerate(P):
    #Starts with ans = 0 + 0.49 * np.log2(0.49)
    ans += prob * np.log2(prob)
    #print(f"Entropy sum at S{probIndex} is", ans)
ans = -ans

#Both are the same answer
#print(-np.sum(P * np.log2(P)))
print('Entropy is', ans)
