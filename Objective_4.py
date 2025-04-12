import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
columns = ['Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']
category = 'srcStateName'  

fig, axes = plt.subplots(2, 2, figsize=(12,8))
axes = axes.flatten()


for i, col in enumerate(columns):
    sns.barplot(
        data=df.sort_values(by=col, ascending=False).head(25),  
        x=col,
        y=category,
        ax=axes[i],
        hue=category,
        palette='rocket'  
    )
    axes[i].set_title(f'Top 10 by {col}')
    axes[i].set_xlabel(f'{col} Value')
    axes[i].set_ylabel('')

plt.tight_layout()
plt.show()
