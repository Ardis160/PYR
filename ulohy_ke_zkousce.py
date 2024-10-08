#skalovani, normalizovani, standardizace

from sklearn.preprocessing import MinMaxScaler, Normalizer, StandardScaler
from scipy.stats import boxcox
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(drop="first")
df = pd.read_csv("catalog.csv")

df2 = pd.DataFrame.sparse.from_spmatrix(encoder.fit_transform(df))

print(df2.head())
