import pandas as pd
import numpy as np

# Read dataset
df = pd.read_csv("data/samplesuperstore.csv", encoding='latin1')

print("Original Dataset Shape:", df.shape)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create new columns
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Profit Margin
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

# Replace infinite values
df.replace([np.inf, -np.inf], 0, inplace=True)

# Data validation
df = df[df['Sales'] >= 0]
df = df[df['Quantity'] >= 0]

# Rename columns for SQL compatibility
df.columns = df.columns.str.replace(' ', '_')

# Save cleaned dataset
df.to_csv("data/cleaned_superstore.csv", index=False)

print("Data Transformation Completed Successfully")
print("Cleaned Dataset Shape:", df.shape)

print(df.head())