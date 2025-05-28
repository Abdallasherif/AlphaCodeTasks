import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1-2: Load dataset and clean Price column
df = pd.read_csv('Books.csv')
df['Price'] = df['Price'].replace('[£]', '', regex=True).astype(float)

# Step 3-4: Basic info and stats
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())

print("Average price:", df['Price'].mean())
print("Median price:", df['Price'].median())
print("Most expensive book price:", df['Price'].max())
print("Cheapest book price:", df['Price'].min())

print("Availability counts:")
print(df['Availability'].value_counts())

print("Most popular books (by Title count):")
print(df['Title'].value_counts())

print("Missing values per column:")
print(df.isnull().sum())

print("Duplicate rows count:", df.duplicated().sum())

# Step 5: Convert 'Rate' column from words to numbers
rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}
df['Rate'] = df['Rate'].map(rating_map)

print("Value counts of 'Rate':")
print(df['Rate'].value_counts())

# Step 6: Visualizations

# Distribution of prices
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=20, kde=True, color='teal')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.grid(True)
plt.show()

# Boxplot of prices
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Price'], color='teal')
plt.title('Boxplot of Book Prices')
plt.xlabel('Price (£)')
plt.grid(True)
plt.show()

# Stock availability count
plt.figure(figsize=(6, 4))
sns.countplot(x='Availability', data=df, palette='Set2')
plt.title('Stock Availability of Books')
plt.xlabel('Availability')
plt.ylabel('Number of Books')
plt.xticks(rotation=15)
plt.grid(True)
plt.show()

# Price vs Rating boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x='Rate', y='Price', data=df, palette='Set2')
plt.title('Price vs. Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.grid(True)
plt.show()

# Correlation heatmap of numeric columns
numeric_df = df.select_dtypes(include=[np.number])
plt.figure(figsize=(6, 4))
sns.heatmap(numeric_df.corr(), annot=True, cmap='YlGnBu')
plt.title('Correlation Matrix (Numeric Features Only)')
plt.show()

# --- Step 7: Detect problems ---

print("Missing values per column:")
print(df.isnull().sum())

print("Number of duplicated rows:", df.duplicated().sum())

print("Unique values in 'Availability':", df['Availability'].unique())

# Detect outliers in Price using IQR
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Price'] < (Q1 - 1.5 * IQR)) | (df['Price'] > (Q3 + 1.5 * IQR))]
print(f"Number of outliers detected in Price: {outliers.shape[0]}")
print("Outliers preview:")
print(outliers[['Title', 'Price', 'Rate']])

# --- Step 9: Find relationships & insights ---

print("Correlation between Price and Rate:")
print(df[['Price', 'Rate']].corr())

# Average Price by Rating
avg_price_by_rate = df.groupby('Rate')['Price'].mean().reset_index()
print("Average Price by Rating:")
print(avg_price_by_rate)

plt.figure(figsize=(8, 5))
sns.barplot(x='Rate', y='Price', data=avg_price_by_rate, palette='coolwarm')
plt.title('Average Book Price by Rating')
plt.xlabel('Rating (Stars)')
plt.ylabel('Average Price (£)')
plt.show()

# Count of books per Rating
plt.figure(figsize=(8, 5))
sns.countplot(x='Rate', data=df, palette='Set3')
plt.title('Count of Books per Rating')
plt.xlabel('Rating (Stars)')
plt.ylabel('Number of Books')
plt.show()

# Top 5 most expensive books
print("Top 5 most expensive books:")
print(df.sort_values(by='Price', ascending=False)[['Title', 'Price', 'Rate']].head())

# Top 5 cheapest books
print("Top 5 cheapest books:")
print(df.sort_values(by='Price', ascending=True)[['Title', 'Price', 'Rate']].head())
