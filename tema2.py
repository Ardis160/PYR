import pandas as pd
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("NFL Play by Play 2009-2016 (v3).csv")
missing_values = df.isnull().sum()
print(missing_values)

df['Date'] = df['Date'].str.cat(df['time'], sep=" ")
df.rename(columns={'Date': 'DateTime'}, inplace=True)
df.drop(columns=['time'], inplace=True)

df['desc'] = df['desc'].str.replace(
    "([A-Z]\.[A-Z][a-z]+(\s[A-Z][a-z]+)?)|(#[0-9]+\s(([A-Z]+\s[A-Z]+)|([A-Z][a-z]+)|([A-Z]\.\s?[A-Z][a-z]+)))",
    "CENZUROVÁNO",
    regex=True
)
print(df['desc'])
pattern = r"\(((?!.*[:]\d+|CENZUROVÁNO|[A-Z]\.[A-Z][a-z]+(?:\s[A-Z][a-z]+)?|#[0-9]+\s(?:[A-Z]+\s[A-Z]+|[A-Z][a-z]+|[A-Z]\.\s?[A-Z][a-z]+))[^()]*)\)"

df['Strategy'] = df['desc'].str.extract(pattern, expand=False)

before_delete = len(df['Strategy'])
after_delete = len(df['Strategy'].dropna(axis=0))
print("Smazáním řádků bez strategie jsme přišli o ", ((before_delete - after_delete)/before_delete)*100," % dat")

col_before = len(df.axes[1])
df2 = df.dropna(axis=1)
col_after = len(df2.axes[1])
print("Smazáním sloupců s chybějícími hodnotami jsme přišli o ",((col_before - col_after)/col_before)*100," % dat")


df3 = df.fillna(0).drop_duplicates()
df4 = df.fillna(method="ffill").fillna(method='bfill').drop_duplicates()
imputer = SimpleImputer(strategy="mean")
dfnum = df.select_dtypes(include='number')
df5 = pd.DataFrame(imputer.fit_transform(dfnum), columns=dfnum.columns).drop_duplicates()
print(dfnum.describe())

plt.figure(figsize=(8, 6))
plt.subplot(1, 3, 1)
sns.scatterplot(data=dfnum, x='FieldGoalDistance', y='yacWPA')
plt.title('FieldGoalDistance vs yacWPA')

plt.subplot(1, 3, 2)
sns.scatterplot(data=dfnum, x='yacWPA', y='airWPA')
plt.title('yacWPA vs airWPA')

plt.subplot(1, 3, 3)
sns.scatterplot(data=dfnum, x='airWPA', y='FieldGoalDistance')
plt.title('airWPA vs FieldGoalDistance')
plt.show()

field_goal = pd.concat([
    df3[['FieldGoalDistance']].assign(Strategy="Nahrazení nulou"),
    df4[['FieldGoalDistance']].assign(Strategy="Dopředné doplnění"),
    df5[['FieldGoalDistance']].assign(Strategy="Nahrazení průměrem")
])

yacWPA = pd.concat([
    df3[['yacWPA']].assign(Strategy="Nahrazení nulou"),
    df4[['yacWPA']].assign(Strategy="Dopředné doplnění"),
    df5[['yacWPA']].assign(Strategy="Nahrazení průměrem")
])

airWPA = pd.concat([
    df3[['airWPA']].assign(Strategy="Nahrazení nulou"),
    df4[['airWPA']].assign(Strategy="Dopředné doplnění"),
    df5[['airWPA']].assign(Strategy="Nahrazení průměrem")
])

plt.figure(figsize=(10, 6))
sns.histplot(data=field_goal, x="FieldGoalDistance", hue="Strategy", bins=15, kde=False, element="step", stat="count", alpha=0.6)
plt.title("Různé strategie pro doplnění NA hodnot FieldGoalDistance")
plt.xlabel("FieldGoal Distance")
plt.ylabel("Počet výskytů")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=yacWPA, x="yacWPA", hue="Strategy", bins=15, kde=False, element="step", stat="count", alpha=0.6)
plt.title("Různé strategie pro doplnění NA hodnot yacWPA")
plt.xlabel("yacWPA")
plt.ylabel("Počet výskytů")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=airWPA, x="airWPA", hue="Strategy", bins=15, kde=False, element="step", stat="count", alpha=0.6)
plt.title("Různé strategie pro doplnění NA hodnot airWPA")
plt.xlabel("airWPA")
plt.ylabel("Počet výskytů")
plt.show()

plt.figure(figsize=(8, 6))
plt.pie(df['Strategy'].value_counts(dropna=False).head(12), labels=None, autopct='%1.1f%%')
plt.legend(df['Strategy'].value_counts(dropna=False).head(12).index, title="Strategie", loc="best", bbox_to_anchor=(1, 0.5))
plt.show()

