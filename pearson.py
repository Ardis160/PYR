import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

data = pd.read_csv("Steam_2024_bestRevenue_1500.csv")

sns.lmplot(x='avgPlaytime', y='revenue', data=data, height=6, aspect=1.5)
plt.title('Scatter plot of Avg Playtime vs Revenue')
plt.xlabel('Average Playtime')
plt.ylabel('Revenue')
plt.show()

correlation_test = pg.corr(data['avgPlaytime'], data['revenue'], alternative='two-sided')
print(correlation_test)