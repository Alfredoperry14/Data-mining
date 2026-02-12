import matplotlib.pyplot as plt
# In data: Min = 13, Max = 70
data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35,
35, 35, 36, 40, 45, 46, 52, 70]
"""

# Q1 = 20
# Median = 25
# Q3 = 35
# IQR = 35-20 = 15
# Lower Limit = 20 - 1.5 * 15 = -2.5
# Upper Limit = 35 + 1.5 * 15 = 57.5
# My upper limit whisker is 52 and 70 is an outlier

"""
bp = plt.boxplot(
    data,
    boxprops=dict(linewidth=2),
    medianprops=dict(color = 'orange', linewidth=2), #Color of median
    whiskerprops=dict(linewidth=2),
    capprops=dict(linewidth=2),
    flierprops=dict(marker='o', #What outliers are labled as
    markersize=8),
    showfliers=True,
)
plt.ylabel('Age Attribute')
plt.title("Problem 1")

fliers = bp['fliers'][0]
x, y = fliers.get_xdata(), fliers.get_ydata()

#There is only going to be one outlier here
for xi, yi in zip(x, y):
    plt.annotate(
        f"Outlier: {yi}",
        (xi, yi),
        xytext=(5, -20),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='-')
    )


from matplotlib.lines import Line2D

legend_elements = [
    Line2D([0], [0], color='orange', lw=2, label='Median'),
]

plt.legend(handles=legend_elements)
plt.show()




