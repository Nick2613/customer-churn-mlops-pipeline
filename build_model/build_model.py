import pandas as pd
import logging
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

logging.basicConfig(
    filename="logs/build_model.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def build_and_train_model(data_path):
    try:
        df = pd.read_csv(data_path)
        logging.info(f"✅ Data for model loaded: {df.shape}")

        # Basic cleaning
        df.dropna(inplace=True)
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df.dropna(inplace=True)

        # Encode categorical columns
        label_encoders = {}
        for col in df.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

        X = df.drop("Churn", axis=1)
        y = df["Churn"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        logging.info(f"✅ Model trained successfully with accuracy: {acc:.4f}")
        logging.info("Classification Report:\n" + classification_report(y_test, preds))
        logging.info(f"Confusion Matrix:\n{confusion_matrix(y_test, preds)}")

        os.makedirs("data/models", exist_ok=True)
        with open("data/models/churn_model.pkl", "wb") as f:
            pickle.dump(model, f)

        logging.info("💾 Model saved successfully.")
        return acc
    except Exception as e:
        logging.error(f"❌ Model training failed: {e}")
        raise e
