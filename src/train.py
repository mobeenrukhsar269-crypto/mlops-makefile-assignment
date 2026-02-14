import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Create models directory
os.makedirs("models", exist_ok=True)

# Load features
df = pd.read_csv("features/titanic_features.csv")

# Select features and target
X = df[['pclass','sex','age','fare','embarked','FamilySize','IsAlone','Title']]
y = df['survived']

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save trained model
joblib.dump(model, "models/titanic_model.joblib")
print("Model trained and saved to models/titanic_model.joblib")
