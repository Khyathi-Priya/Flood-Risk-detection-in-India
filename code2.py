#...........Random Forest Classifier for Flood Prediction...................

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("datasetFlood.csv")

# 1. Data Transformation: Convert to Binary Classification (using 0.5 threshold)
df['FloodOccurred'] = (df['FloodProbability'] >= 0.5).astype(int)

# Define Features (X) and Target (y)
X = df.drop(['FloodProbability', 'FloodOccurred'], axis=1)
y = df['FloodOccurred']

# 2. Split Data: Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Initialize and Train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# 4. Predict on the Test Set
y_pred = model.predict(X_test)

# 5. Performance Analysis
dt_accuracy = accuracy_score(y_test, y_pred)
dt_report = classification_report(y_test, y_pred)
dt_conf_matrix = confusion_matrix(y_test, y_pred)

# Output Performance Results
print("=" * 50)
print("--- RANDOM FOREST CLASSIFIER PERFORMANCE ---")
print("=" * 50)
print(f"Accuracy: {dt_accuracy:.4f}")
print("\nConfusion Matrix:")
print(dt_conf_matrix)
print("\nClassification Report:")
print(dt_report)

# 6. Feature Importance Analysis and Visualization
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
top_10_features = feature_importances.head(10).reset_index()
top_10_features.columns = ['Feature', 'Importance']

# Plotting Feature Importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=top_10_features, palette='viridis')
plt.title('Top 10 Feature Importances for Flood Prediction (Random Forest)')
plt.xlabel('Feature Importance Score')
plt.ylabel('Feature')
plt.tight_layout()
plt.show() # In a local environment, use plt.show()
plt.savefig('feature_importance_plot.png', bbox_inches='tight') # Save the image



