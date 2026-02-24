import matplotlib.pyplot as plt
import numpy as np

#Credit Score
credit_score = np.array([500,600,700, 700, 800, 800, 750, 550, 650, 825])
#Interest Rate(%)
interest_rate = np.array([7.31, 6.7, 5.95, 6.4, 5.4, 5.7, 5.9, 7.0, 6.5, 5.7])

#Problem 6
#--- Plot 6 ----

fig, ax6 = plt.subplots()
plt_six = ax6.scatter(credit_score, interest_rate, c='blue', s=50)
plt.title("Basic Scatter Plot")
plt.xlabel("Credit Score")
plt.ylabel("Loan Interest Rate")
plt.show()

#BID: 4, Credit Score: 700, Interest Rate: 6.4
#BID: 7, Credit Score: 750, Interest Rate: 5.9
#BID: 10, Credit Score: 825, Interest Rate: 5.7