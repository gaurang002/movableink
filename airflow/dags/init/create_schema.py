from airflow import DAG
#from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

with DAG(
    dag_id='create_schema',
    start_date=datetime(2025, 4, 24),
    schedule=None,
    catchup=False,
) as dag:
    run_script = SQLExecuteQueryOperator(
        task_id='create_schema',
        sql="select * from ab_role;",
        conn_id='my_postgres_conn',
    )

run_script