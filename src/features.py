import os
import pandas as pd

# Create features directory
os.makedirs("features", exist_ok=True)

# Load processed data
df = pd.read_csv("data/processed/titanic_processed.csv")

# Create new features
df['FamilySize'] = df['sibsp'] + df['parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# Extract title from name
df['Title'] = df['name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Lady','Countess','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona'],'Rare')
df['Title'] = df['Title'].map({'Master':0,'Miss':1,'Ms':1,'Mme':1,'Mlle':1,'Mrs':1,'Mr':2,'Rare':3})

# Save engineered features
df.to_csv("features/titanic_features.csv", index=False)
print("Engineered features saved to features/titanic_features.csv")
