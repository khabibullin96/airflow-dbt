
import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

AIRFLOW_HOME = os.getenv("AIRFLOW_HOME")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 30),
    'retries': 0,
}
test_dag = DAG(
    'test_dbt',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command=f"cd {AIRFLOW_HOME}/dbt/test_project && dbt run --profiles-dir .",
    dag=test_dag
)

dbt_docs_generate = BashOperator(
    task_id='dbt_docs_generate',
    bash_command=f"cd {AIRFLOW_HOME}/dbt/test_project && dbt docs generate --profiles-dir ./ --profile test_project",
    dag=test_dag
)


dbt_run >> dbt_docs_generate 