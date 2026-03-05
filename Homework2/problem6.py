import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Credit Score
credit_score = np.array([500,600,700, 700, 800, 800, 750, 550, 650, 825])
#Interest Rate(%)
interest_rate = np.array([7.31, 6.7, 5.95, 6.4, 5.4, 5.7, 5.9, 7.0, 6.5, 5.7])

#BID: 4, Credit Score: 700, Interest Rate: 6.4
#BID: 7, Credit Score: 750, Interest Rate: 5.9
#BID: 10, Credit Score: 825, Interest Rate: 5.7

# From HW 1 Problem 7:
#Slope is b1 -0.005445378151260503
#Slope is b0 9.999697478991596

b1 = -0.005445378151260503
b0 = 9.999697478991596

test = pd.DataFrame({
    "BorrowerID": [4, 7, 10],
    "CreditScore": [700, 750, 825],
    "ObservedRate": [6.4, 5.9, 5.7]
})

# Predicted interest rate using the model from Problem 7
test["PredictedRate"] = b1 * test["CreditScore"] + b0

# Model error = Predicted - Observed
test["ModelError"] = test["PredictedRate"] - test["ObservedRate"]

print(test)

"""
   BorrowerID  CreditScore  ObservedRate  PredictedRate  ModelError
0           4          700           6.4       6.187933   -0.212067
1           7          750           5.9       5.915664    0.015664
2          10          825           5.7       5.507261   -0.192739

"""