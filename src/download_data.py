import os
import pandas as pd

# Create directory if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Load Titanic dataset from seaborn
import seaborn as sns
titanic = sns.load_dataset("titanic")

# Save raw dataset
titanic.to_csv("data/raw/titanic.csv", index=False)

print("Raw Titanic dataset saved to data/raw/titanic.csv")
