import os
import pandas as pd
import joblib

# Create results directory
os.makedirs("results", exist_ok=True)

# Load model and features
model = joblib.load("models/titanic_model.joblib")
df = pd.read_csv("features/titanic_features.csv")
X = df[['pclass','sex','age','fare','embarked','FamilySize','IsAlone','Title']]

# Predict
predictions = model.predict(X)
df['predicted_survived'] = predictions

# Save predictions
df[['predicted_survived']].to_csv("results/predictions.csv", index=False)
print("Predictions saved to results/predictions.csv")
