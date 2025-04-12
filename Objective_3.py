import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
columns = ['Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']

for col in columns:
    df[col + '_log'] = np.log(df[col] + 1)
fig, axes = plt.subplots(2,2, figsize=(12, 8))
axes=axes.flatten()
colors = ['skyblue', 'seagreen', 'orange', 'violet']  

for i, col in enumerate(columns):
    sns.histplot(data=df, x=col + '_log', ax=axes[i], kde=True, color=colors[i])
    axes[i].set_title(f'Log Transformed: {col}')

plt.tight_layout()
plt.show()
