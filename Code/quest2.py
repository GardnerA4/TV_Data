import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('data_TV.csv')

# Display basic information about the dataset
print("Dataset Overview:\n")
print(data.info())
print("\nFirst Few Rows:\n")
print(data.head())

# Summary statistics for numerical columns
print("\nSummary Statistics for Numeric Columns:\n")
print(data.describe())

# Check for missing values
print("\nMissing Values:\n")
print(data.isnull().sum())

# Most popular shows
print("\nTop 5 Most Popular Shows:\n")
print(data[['name', 'popularity']].sort_values(by='popularity', ascending=False).head())

# Highest-rated shows
print("\nTop 5 Highest-Rated Shows:\n")
print(data[['name', 'vote_average']].sort_values(by='vote_average', ascending=False).head())

# Distribution of vote_average
plt.figure(figsize=(10, 6))
sns.histplot(data['vote_average'], kde=True, bins=20, color='blue')
plt.title('Distribution of Vote Average')
plt.xlabel('Vote Average')
plt.ylabel('Frequency')
plt.show()

# Popularity by original language
plt.figure(figsize=(12, 6))
lang_popularity = data.groupby('original_language')['popularity'].mean().sort_values(ascending=False)
lang_popularity.plot(kind='bar', color='green')
plt.title('Average Popularity by Original Language')
plt.xlabel('Original Language')
plt.ylabel('Average Popularity')
plt.show()

# Top countries producing the shows
plt.figure(figsize=(12, 6))
country_counts = data['origin_country'].value_counts().head(10)
country_counts.plot(kind='bar', color='orange')
plt.title('Top 10 Countries Producing TV Shows')
plt.xlabel('Country')
plt.ylabel('Number of Shows')
plt.show()

# Correlation heatmap for numeric columns
plt.figure(figsize=(8, 6))
correlation = data[['popularity', 'vote_average', 'vote_count']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
