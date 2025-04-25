from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id='create_schema',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["init"],
) as dag:

    create_tables = PostgresOperator(
        task_id="create_tables",
        postgres_conn_id="my_postgres_conn",
        sql="sql/create_schema.sql",
    )
