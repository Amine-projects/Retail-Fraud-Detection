from preprocess import load_data, preprocess_data
from train import train_xgboost, train_random_forest, save_model
from evaluate import evaluate_model
from utils import make_dirs

def main():
    make_dirs()

    df = load_data("data/creditcard.csv")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = train_xgboost(X_train, y_train)
    save_model(model, "models/xgboost.pkl")

    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
