import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/gauri/Downloads/python dataset original csv.csv")
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
columns = ['Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  

axes = axes.flatten()  

for i, col in enumerate(columns):
    axes[i].hist(df[col], bins=20,color='skyblue', edgecolor='black')
    axes[i].set_title(f'Histogram of {col}')
    axes[i].set_xlabel('Frequency')
    axes[i].set_ylabel('Value')

plt.tight_layout()
plt.show()

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

top_states = df.groupby('srcStateName')['Net area sown'].mean().nlargest(10).index
df_melted = df[df['srcStateName'].isin(top_states)][['srcStateName', 'Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']] \
    .melt(id_vars='srcStateName', var_name='Area Type', value_name='Area')


plt.figure(figsize=(18, 10))
sns.boxplot(x='srcStateName', y='Area', hue='Area Type', data=df_melted, palette='Set2')
plt.yscale('log')
plt.xticks(rotation=30, ha='right')
plt.title('Area Distribution by State and Area Type (Top 10 States)')
plt.xlabel('State'); plt.ylabel('Area')
plt.legend(title='Area Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


top_states = df.groupby('srcStateName')['Net area sown'].mean().nlargest(10).index
df_top = df[df['srcStateName'].isin(top_states)]


area_avg = df_top[['Net area sown', 'Area under current fallows',
                   'Net area cultivated', 'Uncultivated area ']].mean()


explode = [0.05] * len(area_avg)  
colors = sns.color_palette("pastel") 


plt.figure(figsize=(8,8))
plt.pie(area_avg, labels=area_avg.index,
        autopct='%1.1f%%',  
        startangle=140,     
        explode=explode,    
        shadow=True,        
        colors=colors,     
        textprops={'fontsize': 14, 'weight': 'bold'})  


plt.title('Average Area Distribution (Top 10 States)', fontsize=16, fontweight='bold')
plt.axis('equal') 
plt.show()


top_states = df.groupby('srcStateName')['Net area sown'].mean().nlargest(10).index
df_top = df[df['srcStateName'].isin(top_states)]
area_avg = df_top[['Net area sown', 'Area under current fallows',
                   'Net area cultivated', 'Uncultivated area ']].mean()

explode = [0.05] * len(area_avg)  
colors = sns.color_palette("Set1") 

plt.figure(figsize=(8,8))
wedges, texts, autotexts = plt.pie(area_avg,
                                   labels=area_avg.index,
                                   autopct='%1.1f%%',
                                   startangle=140,
                                   explode=explode,
                                   shadow=True,
                                   colors=colors,
                                   textprops={'fontsize': 14, 'weight': 'bold'})

centre_circle = plt.Circle((0, 0), 0.40, fc='white')
plt.gca().add_artist(centre_circle)

plt.title('Donut Chart: Average Area Distribution (Top 10 States)', fontsize=16, fontweight='bold')
plt.axis('equal') 
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,8))
sns.scatterplot(
    data=df,
    x='Net area sown',
    y='Net area cultivated',
    hue='srcStateName',
    palette='Set2',
    s=100,  
    alpha=0.8  
)

plt.title('Scatter Plot: Net Area Sown vs Net Area Cultivated', fontsize=16, fontweight='bold')
plt.xlabel('Net Area Sown')
plt.ylabel('Net Area Cultivated')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='State')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

num_cols = ['Net area sown', 'Area under current fallows', 'Net area cultivated', 'Uncultivated area ']


corr = df[num_cols].corr()


plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, linecolor='gray', square=True, cbar_kws={'shrink': 0.7})
plt.title('Correlation Heatmap of Area Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
