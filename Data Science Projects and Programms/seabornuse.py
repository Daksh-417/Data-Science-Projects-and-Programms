import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

# Load a sample dataset
tips = sns.load_dataset("tips")
# sns.histplot(data=tips, x="total_bill")
# plt.show()
# sns.kdeplot(data=tips, x="total_bill")
# plt.show()
# sns.displot(data=tips, x="total_bill", kde=True)

# sns.boxplot(data=tips, x="day", y="total_bill")
# plt.show()
# sns.violinplot(data=tips, x="day", y="total_bill")
# plt.show()
# sns.stripplot(data=tips, x="day", y="total_bill")
# plt.show()
# sns.swarmplot(data=tips, x="day", y="total_bill")
# plt.show()
# sns.barplot(data=tips, x="day", y="total_bill")
# plt.show()
# sns.countplot(data=tips, x="day")
# plt.show()
# sns.pointplot(data=tips, x="day", y="total_bill", hue="sex")
# plt.show()

# sns.regplot(data=tips, x="total_bill", y="tip")
# plt.show()
# sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex")

# flights = sns.load_dataset("flights").pivot("month", "year", "passengers")
# sns.heatmap(flights, annot=True, fmt="d")
# plt.show()
# sns.clustermap(flights)

# g = sns.FacetGrid(tips, col="sex", row="time")
# g.map(sns.histplot, "total_bill")
# sns.pairplot(tips, hue="sex")
# sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg")

# sns.set_theme(style="whitegrid")
# sns.set_palette("pastel")

# x = random.normal(size=(2, 3))
# print(x)
# x = random.normal(loc=1, scale=2, size=(2, 3))
# print(x)

sns.displot(random.normal(size=1000), kind="kde")
plt.show()

sns.barplot(x="sex", y="total_bill", data=tips)
plt.show()

sns.countplot(x="day", data=tips)
plt.show()

sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
plt.show()

sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()

sns.histplot(tips['total_bill'], kde=True)
plt.show()