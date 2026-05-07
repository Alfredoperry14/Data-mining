import numpy as np

mean_a, sigma_a = 35, 2
mean_b, sigma_b = 42, 3

x = 39

def gaussian_pdf(x, mean, sigma):
    ans = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mean)**2 / (2 * sigma**2))
    return ans

print(gaussian_pdf(x, mean_a, sigma_a))
print(gaussian_pdf(x, mean_b, sigma_b))