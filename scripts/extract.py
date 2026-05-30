import pandas as pd

# Read dataset
df = pd.read_csv("data/samplesuperstore.csv", encoding='latin1')

print("Dataset Loaded Successfully")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nDataset Shape")
print(df.shape)