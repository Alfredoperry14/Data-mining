import socket
import matplotlib.pyplot as plt
import numpy as np

#Credit Score
credit_score = np.array([500,600,700, 700, 800, 800, 750, 550, 650, 825])
#Interest Rate(%)
interest_rate = np.array([7.31, 6.7, 5.95, 6.4, 5.4, 5.7, 5.9, 7.0, 6.5, 5.7])

#BorrowerID from 1 to 10
# is i in n
# [1,10]
# where n(score, rate) is the index in credit_score || interest_rate

#Problem 6
#--- Plot 6 ----

fig, ax6 = plt.subplots()
plt_six = ax6.scatter(credit_score, interest_rate, c='blue', s=50)
plt.title("Basic Scatter Plot")
plt.xlabel("Credit Score")
plt.ylabel("Loan Interest Rate")
plt.show()

#Problem 7
#Construct linear regression model. y = mx + b
#Y = B_0 + B_1x
#BorrowerID 11, CreditScore 625, Interest Rate (%) ?
mean_credit_score = np.mean(credit_score) #687.5
mean_interest_rate = np.mean(interest_rate) # 6.256
credit_score_minus_mean_array = credit_score - mean_credit_score #X - x_mean
interest_rate_minus_mean_array = interest_rate - mean_interest_rate#Y - y_mea
"""
#b1 = sxy/sxx
#b1 = sum of           (x-X_mean)(y-Y_mean)
                 Sum  -----------------------
                          (x-X_mean)^2
                          
                          
                          
y_hat = b0 + b1x
"""
xy = credit_score_minus_mean_array * interest_rate_minus_mean_array
#print(xy)
sum_xy = np.sum(xy)
#print(sum_xy)
sum_x_xsqr = np.sum(credit_score_minus_mean_array ** 2)
#print(sum_x_xsqr)

b1 = sum_xy / sum_x_xsqr
#b0 = b0 + b1x
#y_mean
b0 = mean_interest_rate - b1 * mean_credit_score
print('Slope is b1', b1)
print('Slope is b0', b0)

y_pred = b1 * credit_score + b0

#--- Plot 7 ----
fig7, ax7 = plt.subplots()
plt_seven = plt.scatter(credit_score, interest_rate, c='blue', s=50)
ax7.plot(credit_score,y_pred)
#Now adding regression line for data in 2.1
plt.title("Scatter Plot with linear regression")
plt.xlabel("Credit Score")
plt.ylabel("Loan Interest Rate")
plt.show()

#New Data
#BorrowerID 11, CreditScore 625, Interest Rate (%) ?
