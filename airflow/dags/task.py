import os
from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from scripts.snowflake_connect import (create_snowflake_stage,
                                       create_snowflake_table,
                                       load_farmer_to_snowflake,
                                       load_farm_to_snowflake,
                                       load_financial_to_snowflake)
from scripts.save_to_s3 import (save_farm_parquet, save_farmer_parquet,
                                  save_financial_parquet)

default_args = {
    "owner": "adewunmi",
}


with DAG(
    dag_id="dbt_snowflake",
    start_date=datetime(2025, 5, 14),
    default_args=default_args,
) as dag:
    
    snowflake_table = PythonOperator(
        task_id='snowflake_table_creation',
        python_callable=create_snowflake_table,
    )

    create_stage = PythonOperator(
        task_id='create_stage',
        python_callable=create_snowflake_stage,
    )
    
    load_farmer = PythonOperator(
        task_id='farmer_load',
        python_callable=load_farmer_to_snowflake,
    )

    load_farm = PythonOperator(
        task_id='farm_load',
        python_callable=load_farm_to_snowflake,
    )

    load_financial = PythonOperator(
        task_id='financial_history_extraction',
        python_callable=load_financial_to_snowflake,
    )

    generate_farm = PythonOperator(
        task_id='farm_generate',
        python_callable=save_farm_parquet,
    )

    data_farmer_generate = PythonOperator(
        task_id='farmer_data_generate',
        python_callable=save_farmer_parquet,
    )

    financial_hist = PythonOperator(
        task_id='financial_history_table',
        python_callable=save_financial_parquet,
    )

    [generate_farm, data_farmer_generate, financial_hist] >> snowflake_table
    snowflake_table >> create_stage >> [load_farm, load_farmer, load_financial]