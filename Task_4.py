#Question__1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("/content/menu.csv")

#Question__2
df.head()
columns = ["Calories", "Total Fat", "Carbohydrates", "Dietary Fiber",
           "Sugars", "Protein", "Vitamin A (% Daily Value)",
           "Vitamin C (% Daily Value)", "Calcium (% Daily Value)",
           "Iron (% Daily Value)"]
display = df[columns].max()
print(display)

#Question__3
selected_columns = ["Calories", "Total Fat", "Carbohydrates", "Dietary Fiber",
                     "Sugars", "Protein", "Vitamin A (% Daily Value)",
                     "Vitamin C (% Daily Value)", "Calcium (% Daily Value)",
                     "Iron (% Daily Value)"]

print(selected_columns)

selected_data = df[selected_columns]

matrix = selected_data.corr()
sns.heatmap(data=matrix)

plt.show()

#Question__4
sns.boxplot(x='Calories', y='Category', data=df)
plt.show()

#Question__5
max_values_items = {column: df.loc[df[column].idxmax()] for column in selected_columns}

summary_link = {column: f"{max_values_items[column]['Item']} - {max_values_items[column][column]}" for column in selected_columns}
summary_link

#Question__6
selected_columns =["Calories", "Total Fat", "Carbohydrates", "Dietary Fiber",
           "Sugars", "Protein", "Vitamin A (% Daily Value)",
           "Vitamin C (% Daily Value)", "Calcium (% Daily Value)",
           "Iron (% Daily Value)"]

plt.figure(figsize=(20, 15))

for i, attribute in enumerate(selected_columns, 1):
    plt.subplot(5, 2, i)
    sns.stripplot(x='Category', y=attribute, data = df, jitter=True)
    plt.title(f'Strip Plot of {attribute} by Category')
    plt.xlabel('Category')
    plt.ylabel(attribute)
    plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

#Question__7
categories = df['Category'].unique()

fig, axes = plt.subplots(len(categories), 1, figsize=(10, 10 * len(categories)))

if len(categories) == 1:
    axes = [axes]

for ax, category in zip(axes, categories):
    category_df = df[df['Category'] == category]

    category_df = category_df.sort_values('Calories', ascending=True)

    ax.barh(category_df['Item'], category_df['Calories'], color='skyblue')
    ax.set_title(f'Calories in items for {category}')
    ax.set_xlabel('Calories')
    ax.set_ylabel('Items')
    ax.set_xlim(0, df['Calories'].max() + 50)

    ax.tick_params(axis='y', labelsize=8)

plt.tight_layout()
plt.show()









