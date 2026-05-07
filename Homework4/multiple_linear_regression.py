"""
Note: You need to organize the first, second attributes and a bias in the form of columns of a
data matrix X, and the price attribute, y, as a separate column vector, and use the multi-variable
linear regression formula to compute the vector 𝛽 = [𝛽0 𝛽1 𝛽2]𝑇.
Interpretation
• β₁ (size) → price increase per square foot
• β₂ (bedrooms) → price contribution per room
• Model predicts price linearly in 2D feature space


"""
import numpy as np
x_matrix = np.array([

    [1, 1500, 3],

    [1, 1600, 3],

    [1, 1700, 3],

    [1, 1800, 4],

    [1, 2000, 4]

])

y_matrix = np.array([300, 320, 340, 360, 400]).reshape(-1, 1)

#Use normal equation
# Normal equation: beta = (X^T X)^(-1) X^T y
beta = np.linalg.inv(x_matrix.T @ x_matrix) @ x_matrix.T @ y_matrix

beta0 = beta[0][0]
beta1 = beta[1][0]
beta2 = beta[2][0]

print(f"\nbeta0 = {beta0}") #0
print(f"beta1 = {beta1}") #0.2
print(f"beta2 = {beta2}") #0
