import pandas as pd

df = pd.read_csv("catalog.csv")

hlavicka = df.head()
print(df.isnull().sum())

#strategie reseni chybejicich hodnot

#smazani radku/sloupcu s chybejicimi zaznamy
df2 = df.dropna(axis=1)
print(df2)

#doplnovani chybejicich zaanamu
df.fillna(0)
#print(df)

d3 = df.fillna(method="ffill")
#print(d3)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer
dfnum = df.select_dtypes(include='number')
df3 = imputer.fit_transform(dfnum)
#print(df3)