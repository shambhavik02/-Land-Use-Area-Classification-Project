import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

num_cols = ['Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']

corr = df[num_cols].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, linecolor='gray', square=True, cbar_kws={'shrink': 0.7})
plt.title('Correlation Heatmap of Area Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
