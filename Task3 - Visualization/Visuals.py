import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Books.csv')

# Clean the 'Price' column by removing £ and converting to float
df['Price'] = df['Price'].replace('[£]', '', regex=True).astype(float)

# Map ratings to numbers
rating_map = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
df['Rate'] = df['Rate'].map(rating_map)

# Set seaborn style
sns.set(style='whitegrid')

# 1. Distribution of book prices
plt.figure(figsize=(10,6))
sns.histplot(df['Price'], bins=30, kde=True, color='cornflowerblue')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.savefig('price_distribution.png')
plt.show()

# 2. Boxplot of Price by Rating
plt.figure(figsize=(10,6))
sns.boxplot(x='Rate', y='Price', data=df, palette='pastel')
plt.title('Book Price by Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.savefig('price_by_rating.png')
plt.show()

# 3. Count of books by Availability
plt.figure(figsize=(6,4))
sns.countplot(x='Availability', data=df, palette='Set2')
plt.title('Stock Availability of Books')
plt.xlabel('Availability')
plt.ylabel('Number of Books')
plt.savefig('availability_count.png')
plt.show()

# 4. Average price by rating
avg_price_rating = df.groupby('Rate')['Price'].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(x='Rate', y='Price', data=avg_price_rating, palette='muted')
plt.title('Average Book Price by Rating')
plt.xlabel('Rating')
plt.ylabel('Average Price (£)')
plt.savefig('avg_price_by_rating.png')
plt.show()

# 5. Top 10 most frequent book titles
top_titles = df['Title'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(y=top_titles.index, x=top_titles.values, palette='viridis')
plt.title('Top 10 Most Frequent Book Titles')
plt.xlabel('Count')
plt.ylabel('Book Title')
plt.savefig('top_10_titles.png')
plt.show()

# 6. Scatter plot Price vs Rating with jitter to avoid overlapping
plt.figure(figsize=(10,6))
sns.stripplot(x='Rate', y='Price', data=df, jitter=True, palette='Set1')
plt.title('Scatter Plot of Price vs Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.savefig('scatter_price_rating.png')
plt.show()
