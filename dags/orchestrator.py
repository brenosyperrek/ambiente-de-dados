import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from insert_record import main
    main()

default_args = {
    'description': 'Orquestrador para coletar e inserir dados meteorológicos',
    'start_date': datetime(2025, 1, 1),
    'catchup': False,
}

dag = DAG(
    dag_id='weather_api_dbt_orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='fetch_and_insert_weather_data',
        python_callable=safe_main_callable
    )
    
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app/',
        mounts=[
            Mount(source='/home/breno/projetos/weather-data-project/dbt/my_project',
                  target='/usr/app/',
                  type='bind'),
            Mount(source='/home/breno/projetos/weather-data-project/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind')
        ],
        network_mode='weather-data-project_my-network',
        docker_url='unix:///var/run/docker.sock',
        auto_remove='success'
    )
    
    task1 >> task2