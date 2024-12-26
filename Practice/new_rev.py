from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.impute import KNNImputer, IterativeImputer
data  = {
    'color': ['green', 'blue', 'red'],
    'price': [300, 1000, 4000]
}


df = pd.DataFrame(data)
encoder = LabelEncoder()

df['color_label'] = encoder.fit_transform(df['color'])


df['color'] = df['color'].interpolate()

df['color'] = df['color'].fillna(method = 'ffill')
df['color'] = df['color'].fillna(method = 'bfill')


freq_enco = df['color'].value_counts()
df['color_freq'] = df['color'].map(freq_enco)


one_hot = pd.get_dummies(df['color'])


target_enc = df.groupby('color')['price'].mean()
df['color_target'] = df['color'].map(target_enc)




df['color'] = df['color'].fillna(df['color'].mean())
df['color'] = df['color'].fillna(df['color'].median())
df['color'] = df['color'].fillna(df['color'].mode()[0])



imputer = KNNImputer(n_neighbors=2)

df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)


ite_imputer = IterativeImputer(max_iter=10, random_state=0)
mul_imputed = pd.DataFrame(ite_imputer.fit_transform(df), columns=df.columns)





"""
Features of Data frame
- Two dimensional
- Size mutable
- Heterogeneous
- Label based

Imputation techs
- Mode, Median and mean imputation
- Interpolation
- Forward and backwared
- Regression
- K-nearest 


Normalization and Standardization are techniques used to scale and transform numerical features in a dataset
"""





"""
Plotting

plt.figure(figsize=(20,5))
sns.countplot(x='owner_age', data=df, hue='owner_age', palette='color_blind' legend='false')
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.title("Name of the title", fontdict={"size":30, "Family}: serif, "color": 'blue')
plt.xticks(rotation=45)
plt.show()
"""