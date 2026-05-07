import numpy as np

x_col = [1,2,3,4,5,6]
y_col = [0,0,0,1,1,1]

# threshold for X between 3 and 4 for turning from Y turning from 0 to 1
threshold = (3 + 4) / 2 #3.5
"""
#Logistic regression = linear model + sigmoid

Linear score: z = wX + b

0.5 = 1 / 1 + exp(-(wX+b))
1 = 0.5(1 + exp(-(wX+b))
2 = 1 + exp(-(wX+b))
1 = exp(-(wX+b))

ln(e) = 1 

ln(1) = ln(exp(-wX+b))
0 = exp(-(wX+b))


#wX+b=0
#X=-b/w
#b=-Xw
"""
# choose w
w = 1

b = -w * threshold

#3.5=-(-3.5)/1

z = [(w*x + b) for x in x_col]

def sigmoid(z):
    return 1/(1+np.exp(-z))

# probabilities
probs = [sigmoid(val) for val in z]

for x, p in zip(x_col, probs):
    print(f"x={x}, P(Y=1)={p:.4f}")