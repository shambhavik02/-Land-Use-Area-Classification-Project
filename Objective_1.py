import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel('File.xlsx')
df.head(1)
print(df.dtypes)
print(df.shape)
print("Null values: ",df.isnull().sum())
print(df.describe())
import seaborn as sns
import matplotlib.pyplot as plt
columns = ['Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']

for col in columns:
    sns.histplot(data=df, x=col, kde=False, bins=10, label=col, alpha=0.5)

plt.show()
