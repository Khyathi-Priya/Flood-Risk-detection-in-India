<div align="center">

# 🌊 Flood Risk Detection in India — Random Forest Classifier

**A machine learning system that predicts flood occurrence from environmental and geographical factors, and identifies the key drivers behind flood risk.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

[![GitHub stars](https://img.shields.io/github/stars/Khyathi-Priya/Flood-Risk-detection-in-India?style=flat&color=6C63FF)](https://github.com/Khyathi-Priya/Flood-Risk-detection-in-India/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Khyathi-Priya/Flood-Risk-detection-in-India?style=flat&color=6C63FF)](https://github.com/Khyathi-Priya/Flood-Risk-detection-in-India/network)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

</div>

---

## 📌 Overview

Floods are among the most frequent and damaging natural disasters in India, making early risk detection critical for disaster preparedness. This project builds a **flood risk prediction system** that:

- 📊 Uses environmental and geographical features to assess flood likelihood
- 🤖 Classifies flood risk as **Flood / No Flood** using a trained **Random Forest Classifier**
- 🧠 Identifies the **top contributing factors** behind flood occurrence through feature importance analysis
- 📈 Evaluates performance using accuracy, precision, recall, F1-score, and a confusion matrix

> Built using a flood probability dataset, transformed into a binary classification problem for flood risk detection.

---

## 🧠 System Architecture

```
Flood Dataset
(Environmental & Geographical Features + Flood Probability)
        ↓
Target Transformation
  (Flood Probability → Binary Flood Label)
        ↓
Train/Test Split (80/20)
        ↓
ML Model — Random Forest Classifier
  (100 Trees, Balanced Class Weights)
        ↓
Prediction Output (Flood / No Flood)
        ↓
Performance Evaluation + Feature Importance Analysis
```

---

## 📂 Dataset

The dataset contains various **flood-related environmental and geographical features**, along with a target column:

- **FloodProbability** → Continuous probability of flood occurrence

### Target Transformation

The continuous flood probability is converted into a binary classification target:

| Flood Probability | Flood Occurred |
|---|---|
| < 0.5 | 0 (No Flood) |
| ≥ 0.5 | 1 (Flood) |

---

## 🤖 ML Model — Random Forest Classifier

The core prediction engine is a **Random Forest Classifier** trained on the transformed flood dataset.

### Why Random Forest?
- Handles a large number of environmental/geographical features effectively
- Robust to noise and outliers in real-world flood data
- Provides feature importance scores for interpretability
- Resistant to overfitting compared to a single decision tree

### Training Pipeline (`code2.py`)

```
Raw CSV Data (Flood Dataset)
        ↓
Data Loading & Preprocessing
  → Convert Flood Probability into binary labels
        ↓
Train/Test Split (80/20)
        ↓
Random Forest Training
  → n_estimators: 100 trees
  → class_weight: balanced
  → random_state: 42
        ↓
Prediction on Test Set
        ↓
Evaluation + Feature Importance Analysis
```

### How Predictions Work

At inference time (`code2.py`):
1. Flood-related features are loaded and preprocessed
2. The Random Forest model is trained on the 80% training split
3. Predictions are generated on the held-out 20% test set
4. Predictions are evaluated and the top 10 most influential features are identified and visualized

---

## 📊 Evaluation Metrics

The model is evaluated using:

- ✅ Accuracy Score
- ✅ Confusion Matrix
- ✅ Precision
- ✅ Recall
- ✅ F1 Score
- ✅ Classification Report

![Evaluation metric](pictures/Screenshot%202026-06-19%20194843.png)
---

## 📈 Feature Importance Analysis

The project identifies and visualizes the **top 10 most important features** influencing flood prediction, using a feature importance bar chart generated from the trained Random Forest model.

![Feature important score](pictures/Screenshot%202026-06-19%20194816.png)
---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Khyathi-Priya/Flood-Risk-detection-in-India.git
cd Flood-Risk-detection-in-India
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Project
```bash
python code2.py
```

---

## 📁 Project Structure

```
Flood-Risk-detection-in-India/
│
├── datasetFlood.csv          # Flood dataset
├── code2.py                  # Data preprocessing, training & evaluation script
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Scikit-learn | Random Forest Classifier & evaluation metrics |
| Pandas | Data loading & preprocessing |
| Matplotlib | Feature importance visualization |
| Seaborn | Statistical data visualization |

---

## 🎯 Applications

- 🚨 Disaster Management
- ⏱️ Early Flood Warning Systems
- 🌍 Environmental Monitoring
- 📊 Risk Assessment
- 🏙️ Smart City Planning

---

## 🚀 Future Enhancements

- [ ] Compare multiple machine learning algorithms
- [ ] Hyperparameter tuning for improved performance
- [ ] Real-time flood prediction system
- [ ] Web application deployment using Streamlit
- [ ] Integration with live weather APIs
- [ ] Geographic visualization of flood-prone regions

---

## 👩‍💻 Author

**Khyathi Priya Kamireddi**
B.Tech — Computer Science Engineering (AI & ML)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Khyathi-Priya)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khyathi-priya-kamireddi-83144a2b8/)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
