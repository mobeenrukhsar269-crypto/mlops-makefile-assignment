import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Create processed directory
os.makedirs("data/processed", exist_ok=True)

# Load raw data
df = pd.read_csv("data/raw/titanic.csv")

# Fill missing values
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Encode categorical variables
le_sex = LabelEncoder()
df['sex'] = le_sex.fit_transform(df['sex'])

le_embarked = LabelEncoder()
df['embarked'] = le_embarked.fit_transform(df['embarked'])

# Scale numerical features (optional)
scaler = StandardScaler()
numerical_features = ['age', 'fare', 'sibsp', 'parch']
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Save processed dataset
df.to_csv("data/processed/titanic_processed.csv", index=False)
print("Processed dataset saved to data/processed/titanic_processed.csv")
