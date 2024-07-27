# airflow/dags/weather_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# Import the produce_weather_data function
from src.producers.weather_producer import produce_weather_data
from src.consumers.weather_consumer import consume_weather_data

default_args = {
    'owner': 'nassim',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def produce_weather_data():
    os.system('python ../producers/weather_producer.py')

def consume_weather_data():
    os.system('python /path/to/your/project/src/consumers/weather_consumer.py')

dag = DAG(
    'weather_dag',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule_interval=timedelta(minutes=5),
)

t1 = PythonOperator(
    task_id='produce_weather_data',
    python_callable=produce_weather_data,
    dag=dag,
)

t2 = PythonOperator(
    task_id='consume_weather_data',
    python_callable=consume_weather_data,
    dag=dag,
)

t1 >> t2

