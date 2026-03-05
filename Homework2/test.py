import numpy as np, math

def gaussian(x, mu, sigma):
    return 1.0/(math.sqrt(2*math.pi)*sigma) * np.exp(-0.5*((x-mu)/sigma)**2)

def l1_distance(mu1,s1,mu2,s2, xmin, xmax, n=20000):
    x = np.linspace(xmin, xmax, n)
    y1 = gaussian(x, mu1, s1)
    y2 = gaussian(x, mu2, s2)
    dx = x[1]-x[0]
    D = np.sum(np.abs(y1-y2)) * dx    # L1 distance
    TV = D/2.0                        # total variation (0..1)
    overlap = 1.0 - TV                # overlap area (0..1)
    return D, TV, overlap

# Numbers from Table 4.9
mu_h_no, sigma_h_no = 74.60, 7.89
mu_h_yes, sigma_h_yes = 73.00, 6.16
mu_t_no, sigma_t_no = 84.00, 9.62
mu_t_yes, sigma_t_yes = 78.22, 9.88

# ranges
h_xmin = 0
h_xmax = 125
t_xmin = 0
t_xmax = 125

D_h, TV_h, overlap_h = l1_distance(mu_h_no,sigma_h_no, mu_h_yes,sigma_h_yes, h_xmin, h_xmax)
D_t, TV_t, overlap_t = l1_distance(mu_t_no,sigma_t_no, mu_t_yes,sigma_t_yes, t_xmin, t_xmax)

print("Humidity:   L1 D = {:.4f}, TV = {:.4f}, overlap = {:.3%}".format(D_h, TV_h, overlap_h))
print("Temperature:L1 D = {:.4f}, TV = {:.4f}, overlap = {:.3%}".format(D_t, TV_t, overlap_t))