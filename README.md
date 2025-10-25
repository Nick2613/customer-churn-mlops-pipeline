# customer-churn-mlops-pipeline

customer-churn-mlops-pipeline/
│
├── data/
│   ├── raw_data_storage/              # Raw data before processing
│   ├── data_ingestion/                # Data ingestion scripts
│   ├── data_validation/               # Data validation and schema checks
│   ├── data_preparation/              # Cleaning and preprocessing
│   ├── data_transformation_storage/   # Feature engineering and transformation
│   ├── data_versioning/               # DVC integration for version control
│   └── feature_store/                 # SQLite/Feature store database
│
├── build_model/                       # Model training, evaluation, and storage
├── reports/                           # Model metrics and performance reports
├── logs/                              # Log files for each pipeline stage
├── main_pipeline.py                   # Main orchestrator script
├── requirements.txt                   # Dependencies
└── README.md                          # Project documentation

