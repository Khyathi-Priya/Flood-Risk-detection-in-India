# 🌊 Flood Prediction Using Random Forest Classifier

## 📌 Project Overview

This project uses a **Random Forest Classifier** to predict the occurrence of floods based on environmental and geographical factors. The model transforms flood probability values into a binary classification problem and predicts whether a flood is likely to occur.

The project also performs feature importance analysis to identify the most influential factors contributing to flood prediction.

---

## 🚀 Features

- Data preprocessing and transformation
- Binary flood classification using thresholding
- Random Forest machine learning model
- Model performance evaluation
- Confusion matrix generation
- Classification report analysis
- Feature importance visualization
- Top 10 important feature identification

---

## 📂 Dataset

The dataset contains various flood-related features and a target column:

- **FloodProbability** → Probability of flood occurrence

### Target Transformation

The project converts flood probability into a binary target:

| Flood Probability | Flood Occurred |
|------------------|---------------|
| < 0.5 | 0 (No Flood) |
| ≥ 0.5 | 1 (Flood) |

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

---

## 📋 Project Workflow

### 1. Data Loading
Load the flood dataset using Pandas.

### 2. Data Transformation
Convert the continuous flood probability values into binary classes.

### 3. Train-Test Split
Split the dataset into:
- 80% Training Data
- 20% Testing Data

### 4. Model Training
Train a Random Forest Classifier with:
- 100 Decision Trees
- Balanced Class Weights
- Random State = 42

### 5. Prediction
Predict flood occurrence on the test dataset.

### 6. Performance Evaluation
Evaluate the model using:
- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1 Score
- Classification Report

### 7. Feature Importance Analysis
Identify and visualize the top 10 most important features influencing flood prediction.

---

## 📊 Evaluation Metrics

The model performance is measured using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📈 Feature Importance Visualization

The project generates a bar chart showing the top 10 most important features contributing to flood prediction.

---

## 📁 Project Structure

```bash
Flood-Prediction/
│
├── datasetFlood.csv
├── code2.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/Khyathi-priya/code2.git
cd code2.py
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python code2.py
```

---

## 📷 Sample Output

```text
==================================================
--- RANDOM FOREST CLASSIFIER PERFORMANCE ---
==================================================

Accuracy: 0.95

Confusion Matrix:
[[... ...]
 [... ...]]

Classification Report:
precision    recall    f1-score
...
```

---

## 🎯 Applications

- Disaster Management
- Early Flood Warning Systems
- Environmental Monitoring
- Risk Assessment
- Smart City Planning

---

## 🔮 Future Enhancements

- Compare multiple machine learning algorithms
- Hyperparameter tuning
- Real-time flood prediction system
- Web application deployment using Streamlit
- Integration with weather APIs

---

## 👩‍💻 Author

**Khyathi Priya Kamireddi**

Computer Science Engineering (AI & ML)

---
⭐ If you found this project useful, consider giving it a star!
