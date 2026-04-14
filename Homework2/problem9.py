import numpy as np
import matplotlib.pyplot as plt

#Values from Table 4.9

# Humidity
mu_h_no = 74.60
sigma_h_no = 7.89

mu_h_yes = 73.00
sigma_h_yes = 6.16

# Temperature
mu_t_no = 84.00
sigma_t_no = 9.62

mu_t_yes = 78.22
sigma_t_yes = 9.88

#Gaussian probability density function
def gaussian_pdf(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * \
           np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

#Humidity Plot
#np.linespace creates 400 evenly spaced numbers between 50 and 100
x_h = np.linspace(50, 100, 400)

plt.figure()
plt.plot(x_h, gaussian_pdf(x_h, mu_h_no, sigma_h_no), label="Play = No")
plt.plot(x_h, gaussian_pdf(x_h, mu_h_yes, sigma_h_yes), label="Play = Yes")

plt.title("Gaussian PDF of Humidity")
plt.xlabel("Humidity")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()


#Temperature Plot
#np.linespace creates 400 evenly spaced numbers between 45 and 115
x_t = np.linspace(45, 115, 400)

plt.figure()
plt.plot(x_t, gaussian_pdf(x_t, mu_t_no, sigma_t_no), label="Play = No")
plt.plot(x_t, gaussian_pdf(x_t, mu_t_yes, sigma_t_yes), label="Play = Yes")

plt.title("Gaussian PDF of Temperature")
plt.xlabel("Temperature")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()

"""
For part b the temperature is a greater predictor for whether we play or not because there is more of a total variance
than in humidity
"""

import pandas as pd
import numpy as np

df = pd.read_csv("golf_dataset.csv")

# We don't need the ID column
df = df.drop(columns=["ID"])

def entropy(y):
    #Normalize = true returns the probabilities for each value in y. (Y or N)
    probs = y.value_counts(normalize=True)
    return -(probs * np.log2(probs)).sum()

base_entropy = entropy(df["Play"])
print("Base entropy:", base_entropy)


# If we are looking at outlook the features would be Sunny, Rainy, Overcast
def info_gain_categorical(df, feature, target="Play"):
    #Get the entropy for the Play category
    base = entropy(df[target])
    weighted = 0
    for _, sub in df.groupby(feature):

        # For each value of the feature (Sunny, Rain, Overcast),
        # compute the entropy of the target (Play) within that subset.
        # entropy(sub[target]) is all rows where sunny, rainy, etc
        weighted += (len(sub)/len(df)) * entropy(sub[target])
    return base - weighted

def best_info_gain_numeric(df, feature, target="Play"):
    #Base entropy of play before split
    base = entropy(df[target])

    values = np.sort(df[feature].unique())
    #Finding the split between values to cleanly seperate
    thresholds = []

    for i in range(len(values) - 1):
        midpoint = (values[i] + values[i + 1]) / 2
        thresholds.append(midpoint)

    #Information gain is always >= 0
    best_ig = -1
    best_t = None

    for t in thresholds:
        left = df[df[feature] <= t]
        right = df[df[feature] > t]
        if len(left) == 0 or len(right) == 0:
            continue
        # Compute entropy after splitting at the threshold.
        # This is the weighted average entropy of the left and right groups.
        weighted = (len(left)/len(df)) * entropy(left[target]) + (len(right)/len(df)) * entropy(right[target])
        ig = base - weighted

        #With the most information gained we need to keep track of the threshold
        if ig > best_ig:
            best_ig = ig
            best_t = t

    return best_ig, best_t

""" 
# IG for categorical features
ig_outlook = info_gain_categorical(df, "Outlook")
ig_wind = info_gain_categorical(df, "Wind")

# IG for numeric features (also returns best threshold)
ig_hum, t_hum = best_info_gain_numeric(df, "Humidity")
ig_temp, t_temp = best_info_gain_numeric(df, "Temperature")

print("IG(Outlook):", ig_outlook)
print("IG(Wind):", ig_wind)
print("IG(Humidity):", ig_hum, " best threshold:", t_hum)
print("IG(Temperature):", ig_temp, " best threshold:", t_temp)


Base entropy: 0.9402859586706311
IG(Outlook): 0.24674981977443933
IG(Wind): 0.04812703040826949
IG(Humidity): 0.1134008641811034  best threshold: 84.0
IG(Temperature): 0.10224356360985076  best threshold: 82.5
Entropy 
#Going with outlook since it produced the most information gained
            (Play)
   /            |            |
Sunny        Overcast        Rain 

"""

sunny_df = df[df["Outlook"] == "Sunny"]
overcast_df = df[df["Outlook"] == "Overcast"]
rain_df = df[df["Outlook"] == "Rain"]

"""
print(overcast_df["Play"].value_counts())
print(sunny_df["Play"].value_counts())
print(rain_df["Play"].value_counts())
Overcast only has Yes ("Pure Branch")
"""

#Look at Sunny Branch
print("Sunny counts:\n", sunny_df["Play"].value_counts())

print("Sunny IG(Wind):", info_gain_categorical(sunny_df, "Wind"))
ig_h_sunny, t_h_sunny = best_info_gain_numeric(sunny_df, "Humidity")
ig_t_sunny, t_t_sunny = best_info_gain_numeric(sunny_df, "Temperature")

print("Sunny IG(Humidity):", ig_h_sunny, "t=", t_h_sunny)
print("Sunny IG(Temperature):", ig_t_sunny, "t=", t_t_sunny)

#Look at Rain Branch
print("Rain counts:\n", rain_df["Play"].value_counts())

print("Rain IG(Wind):", info_gain_categorical(rain_df, "Wind"))
ig_h_rain, t_h_rain = best_info_gain_numeric(rain_df, "Humidity")
ig_t_rain, t_t_rain = best_info_gain_numeric(rain_df, "Temperature")

print("Rain IG(Humidity):", ig_h_rain, "t=", t_h_rain)
print("Rain IG(Temperature):", ig_t_rain, "t=", t_t_rain)


"""
Play
no     3
yes    2
Sunny IG(Wind): 0.01997309402197489
Sunny IG(Humidity): 0.4199730940219749 t= 77.5
Sunny IG(Temperature): 0.9709505944546686 t= 77.5
Rain counts:

Play
yes    3
no     2
Name: count, dtype: int64
Rain IG(Wind): 0.9709505944546686
Rain IG(Humidity): 0.3219280948873623 t= 66.5
Rain IG(Temperature): 0.3219280948873623 t= 75.0

From the results, for the sunny branch 
we get the most information gained from the Temperature when the threshold is 77.5.
For the rain branch we get the most results based on the wind 

                FINAL TREE:

                    Outlook
           /            |            |
        Sunny         Overcast       Rain 
          |              |             |
    Temp <= 77.5?       Yes        Is there wind? 
      /       |                       /      |
    True      False              True       False
    Yes        No                No          Yes
"""

print(sunny_df[sunny_df["Temperature"] <= 77.5]["Play"])

# 9d
# In this case the outlook is sunny
# Temperature is given as low so I'm assuming that it's less than 77.5.
# In this case it would be Play = Yes based-on the decision tree

def decision_tree(outlook, temperature, wind):
    if(outlook == "Sunny"):
        if(temperature <= 77.5):
            return True
        else:
            return False
    elif(outlook == "Overcast"):
        return True
    else:
        if(wind == True):
            return False
        return True

#9e
no_15 = decision_tree("Sunny", 76, False)
no_16 = decision_tree("Rainy", 72, True)
print('No 15:', no_15) #For No 15 Play Y = True
print('No 16:', no_16) #For No 16 Play Y = False
