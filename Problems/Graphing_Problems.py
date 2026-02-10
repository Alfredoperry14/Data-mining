import socket
from operator import contains
from typing import List

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

#calculate for BorrowerID 11, CreditScore 625, Interest Rate (%) ?

solved_interest_rate = b1 * 625 + b0
#print("B11's interest rate is", solved_interest_rate)
#B11's interest rate is 6.596336134453781

#--- Plot 7 ----
fig7, ax7 = plt.subplots()
plt_seven = plt.scatter(credit_score, interest_rate, c='blue', s=50)
ax7.plot(credit_score,y_pred)
#Now adding regression line for data in 2.1
plt.title("Scatter Plot with linear regression")
plt.xlabel("Credit Score")
plt.ylabel("Loan Interest Rate")
plt.show()

#Problem 8
# #New Data
#BorrowerID 11, CreditScore 625, Interest Rate (6.59%)
#--- Plot 8----
# New data is BorrowerID 11
# Test Data is BorrowerID 4, 7, 10 (index is = ID - 1)
testIndex = [4,7,10]

fig8, ax8 = plt.subplots()
plt_eight = plt.scatter(credit_score, interest_rate, c='blue')
ax8.plot(credit_score,y_pred)

test_credit = []
test_interest = []
for index in testIndex:
    ax8.scatter(credit_score[index - 1],interest_rate[index - 1], c ='red', s=50)
    test_credit.append(credit_score[index - 1])
    test_interest.append(interest_rate[index - 1])

test_credit = np.array(test_credit)
test_interest = np.array(test_interest)
"""
#Plot with the data from 2.2 also
#ax8.scatter(625, 6.59, c='black', s = 50)
"""

mean_test_credit_score = np.mean(test_credit) #
mean_test_interest_rate = np.mean(test_interest) #
test_credit_minus_mean_array = test_credit - mean_credit_score #X - x_mean
test_interest_minus_mean_array = test_interest - mean_interest_rate#Y - y_mea
"""
#b1 = sxy/sxx
#b1 = sum of           (x-X_mean)(y-Y_mean)
                 Sum  -----------------------
                          (x-X_mean)^2



y_hat = b0 + b1x
"""

xy = test_interest_minus_mean_array * test_credit_minus_mean_array
# print(xy)
sum_test_xy = np.sum(xy)
# print(sum_xy)
sum_test_x_xsqr = np.sum(test_credit_minus_mean_array ** 2)
# print()

b1 = sum_test_xy / sum_test_x_xsqr
# b0 = b0 + b1x
# y_mean
b0 = mean_test_interest_rate - b1 * mean_test_credit_score
print('Slope is b1', b1)
print('Slope is b0', b0)

y_test_pred = b1 * test_credit + b0

ax8.plot(test_credit,y_test_pred, c = 'green')

plt.title("Scatter Plot with both linear regressions of normal and test data")
plt.show()