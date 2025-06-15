import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("C:/Users/HP/Desktop/UnemploymentAnalysiswithPython/Unemployment in India.csv")

# Initial 
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Plot 1: Barplot of average unemployment rate of region
plt.figure(figsize=(12,6))
sns.barplot(x='region', y='estimated_unemployment_rate_(%)', data=df)
plt.xticks(rotation=90)
plt.title('Unemployment Rate by Region')
plt.tight_layout()
plt.show()

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Plot 2: Unemployment trend over time
plt.figure(figsize=(12,6))
sns.lineplot(x='date', y='estimated_unemployment_rate_(%)', data=df, hue='region')
plt.title('Unemployment Trend Over Time by Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Filter data by area (Urban or Rural)
filtered_df = df[df['area'] == 'Urban']  # change to 'Rural' if needed

#  Compute correlation matrix
corr_matrix = filtered_df.corr(numeric_only=True)

#  Styled heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    annot_kws={"size": 12},
    linewidths=0.5,
    linecolor='black'
)
plt.title("Correlation Heatmap (Urban Areas)", fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(rotation=0, fontsize=12)
plt.tight_layout()

#  Save heatmap as image
plt.savefig("heatmap.png", dpi=300)

#  Show the heatmap
plt.show()
