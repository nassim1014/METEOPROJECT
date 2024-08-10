FROM apache/airflow:2.6.3

# Copy requirements.txt from the build context
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Airflow configuration
COPY src/airflow/airflow.cfg /opt/airflow/airflow.cfg

# Copy DAGs
COPY src/airflow/dags /opt/airflow/dags

