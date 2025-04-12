import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel('File.xlsx')
columns = ['Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # 2 rows, 2 columns

axes = axes.flatten()  # flatten to loop easily

for i, col in enumerate(columns):
    axes[i].hist(df[col], bins=20,color='skyblue', edgecolor='black')
    axes[i].set_title(f'Histogram of {col}')
    axes[i].set_xlabel('Frequency')
    axes[i].set_ylabel('Value')

plt.tight_layout()
plt.show()
