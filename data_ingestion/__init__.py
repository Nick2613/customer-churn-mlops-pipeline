class DataIngestionPipeline:
    def run_ingestion(self):
        print("✅ Step 2: Data Ingestion running...")
        return {"csv_file": "data/raw/customers.csv", "huggingface_file": "mock_dataset"}
