from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.utils.email import send_email
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'dn',
    'retries': 5,
    'retry_delay': timedelta(minutes=10),
    'email': ['ndevarapu@outlook.com'],
    'email_on_failure': True,
    'email_on_retry': True
}

with DAG(
        dag_id = 'dag_with_minio_s3_v06',
        start_date = datetime(2024, 3, 9),
        schedule_interval = '@daily',
        default_args = default_args
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='minio_conn',
        mode='poke',
        poke_interval=5,
        timeout=30
    )
