import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename="logs/data_ingestion.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def ingest_data():
    try:
        raw_path = "data/raw_data_storage/WA_Fn-UseC_-Telco-Customer-Churn.csv"
        if not os.path.exists(raw_path):
            raise FileNotFoundError(f"Dataset not found at {raw_path}")

        df = pd.read_csv(raw_path)
        logging.info(f"✅ Data loaded successfully with shape {df.shape}")

        # Save to a clean path for next stage
        os.makedirs("data/data_ingestion", exist_ok=True)
        processed_path = "data/data_ingestion/ingested_data.csv"
        df.to_csv(processed_path, index=False)
        logging.info(f"📁 Data saved to {processed_path}")

        return processed_path
    except Exception as e:
        logging.error(f"❌ Data ingestion failed: {e}")
        raise e
