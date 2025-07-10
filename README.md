# Fraud Detection Project

A machine learning pipeline to detect fraudulent transactions using techniques like data preprocessing, class imbalance handling, and model optimization with XGBoost.

---

##  Project Structure

fraud detection project/
│
├── data/ # Raw and/or processed datasets
├── models/ # Trained models (e.g. xgboost.pkl)
├── notebook/ # Jupyter notebooks for exploration
├── src/ # Source code
│ ├── main.py # Pipeline entry point
│ ├── train.py # Model training logic
│ ├── evaluate.py # Model evaluation
│ ├── preprocess.py # Data preprocessing functions
│ └── utils.py # Utility functions
├── requirements.txt # Required Python packages
└── .gitignore


---

## To use it

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd fraud\ detection\ project







## 2. Create and activate a virtual environment
python -m venv venv
On MacOS/ Linux use : source venv/bin/activate
On Windows use: venv\Scripts\activate

## 3. Install dependencies

pip install -r requirements.txt

# How to Run

python src/main.py

This will:

Load and preprocess the data
Train a fraud detection model using XGBoost
Evaluate and save the model

# Model Details

Algorithm: XGBoost Classifier

Optimizations:

Handled class imbalance using imbalanced-learn

Hyperparameter tuning with optuna

Evaluation Metrics: Accuracy, Precision, Recall, AUC (see evaluate.py)

# Author:

Amine Benmoussa

# License:

This project is open-source and available under the MIT License.
