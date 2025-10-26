# Customer Churn Prediction MLOps Pipeline

A production-ready **MLOps pipeline** for predicting customer churn, orchestrated with **Apache Airflow**, containerized with **Docker**, and using **PostgreSQL** for data storage.

---

## Features

* Automated data ingestion, validation, and feature engineering
* Model training, evaluation, and logging
* Airflow DAGs for workflow orchestration
* Dockerized setup for easy deployment

---

## Tech Stack

* **Python 3.12**, **scikit-learn**, **Pandas/NumPy**
* **Apache Airflow 2.9.3**
* **Docker & Docker Compose**
* **PostgreSQL 15**

---

## Project Structure

```
customer-churn-mlops-pipeline/
├── dags/                      # Airflow DAGs
├── data/                      # Datasets
├── reports/                   # Validation & model reports
├── scripts/                   # Helper scripts
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
```

---

## Setup

```bash
git clone https://github.com/<your-username>/customer-churn-mlops-pipeline.git
cd customer-churn-mlops-pipeline
docker-compose up --build -d
docker exec -it <airflow-webserver> airflow db init
docker exec -it <airflow-webserver> airflow users create \
    --username admin \
    --firstname Nikhil \
    --lastname Rochwani \
    --role Admin \
    --email nnikhilrochwanii@gmail.com
```

---

## Usage

* **Airflow UI:** [http://localhost:8081](http://localhost:8081)
* **Username:** `admin`
* **Trigger DAGs:** `churn_pipeline_dag` to run the full pipeline
* **Monitor logs** in the Airflow UI

---

## Contributing

1. Fork the repo
2. Create a branch
3. Commit & push changes
4. Open a Pull Request

---
