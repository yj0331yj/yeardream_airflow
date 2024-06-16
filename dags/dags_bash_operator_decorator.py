from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator


@dag(
    dag_id="dags_bash_operator",
    schedule="0 13 * * 5#2",
    start_date=pendulum.datetime(2024, 5, 1, tz="Asia/Seoul"),
    tags=["homework"],
    catchup=False
)
def generate_dag():
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
