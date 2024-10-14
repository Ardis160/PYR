import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from seaborn import set_style

sns.set_style("darkgrid")
sns.set_context("talk")
df = pd.read_csv("catalog.csv")
#plt.hist(df.population)
#plt.show()
#sns.histplot(x=df.distance, kde=True)
#sns.barplot(x=df.country_name,y=df.population)

sns.violinplot(x=df.landslide_size, y=df.injuries)
plt.show()
