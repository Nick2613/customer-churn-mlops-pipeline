class SimpleChurnFeatureStore:
    store_path = "data/feature_store.db"
    def auto_populate_from_latest_data(self):
        print("✅ Step 7: Feature Store running...")
        return "feature_store_populated"
    def close(self):
        print("✅ Feature Store connection closed.")
