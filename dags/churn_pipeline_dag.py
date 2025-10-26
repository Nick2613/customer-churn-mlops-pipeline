"""
Churn Pipeline DAG
==================
This DAG orchestrates the end-to-end churn prediction ML pipeline
using Apache Airflow.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": True,
    "email": ["alerts@mlops.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id="churn_prediction_pipeline",
    description="End-to-end Customer Churn Prediction pipeline",
    default_args=default_args,
    schedule_interval="@daily",  # runs once a day
    start_date=datetime(2025, 10, 1),
    catchup=False,
    tags=["mlops", "churn", "training"],
) as dag:

    # Step 1: Check environment and dependencies
    check_env = BashOperator(
        task_id="check_environment",
        bash_command="echo '✅ Airflow environment ready!' && python --version",
    )

    # Step 2: Run the main pipeline
    run_pipeline = BashOperator(
        task_id="run_churn_pipeline",
        bash_command="python /opt/airflow/main_pipeline.py",
    )

    # Step 3: Confirm success
    finish = BashOperator(
        task_id="finish",
        bash_command="echo '🎉 Churn Prediction Pipeline completed successfully!'",
    )

    # Task sequence
    check_env >> run_pipeline >> finish
