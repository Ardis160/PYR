import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

data = pd.read_csv("data.csv")
cor_test = pg.corr(data['year'], data['popularity'], method='pearson')
sns.lmplot(x='year', y='popularity', data=data, height=6, aspect=1.5,
           line_kws={'color': 'red'},   # Červená barva čáry
           scatter_kws={'color': 'blue', 'alpha': 0.6})
plt.show()
corr_matrix = data.select_dtypes(include='number').corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f')
plt.show()