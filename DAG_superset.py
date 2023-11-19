from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import mysql.connector
import random
from datetime import datetime, timedelta

# Define default_args and DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'website_traffic_etl',
    default_args=default_args,
    description='ETL process for website traffic data',
    schedule_interval=timedelta(minutes=15),  # Run every 15 minutes
    catchup=False,
)


# ETL Function
def etl():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ANSKk08aPEDbFjDO",
        database="website_traffic"
    )
    cursor = connection.cursor()

    # Generate and insert synthetic data
    timestamp = datetime.now()
    pageviews = random.randint(100, 1000)
    unique_visitors = random.randint(50, 200)
    cursor.execute("INSERT INTO traffic (timestamp, pageviews, unique_visitors) VALUES (%s, %s, %s)",
                   (timestamp, pageviews, unique_visitors))

    # Commit changes and close the connection
    connection.commit()
    connection.close()


# Define the ETL task
etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=etl,
    dag=dag,
)

# Set task dependencies (if needed)
# etl_task.set_upstream(...)
# ...

if __name__ == "__main__":
    dag.cli()