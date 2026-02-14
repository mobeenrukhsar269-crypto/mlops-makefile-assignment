import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Create results directory (if not exists)
os.makedirs("results", exist_ok=True)

# Load predictions and true labels
df = pd.read_csv("features/titanic_features.csv")
y_true = df['survived']
y_pred = pd.read_csv("results/predictions.csv")['predicted_survived']

# Calculate metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Save metrics
with open("results/metrics.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.4f}\n")
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall: {recall:.4f}\n")
    f.write(f"F1-score: {f1:.4f}\n")

print("Evaluation metrics saved to results/metrics.txt")
