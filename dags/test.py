from airflow import DAG
import datetime
from airflow.operators.bash import BashOperator

my_dag = DAG(
    dag_id="dags_bash_operator_standard",
    schedule_interval="0 9 * * 1,5",  # schedule_interval로 수정
    start_date=datetime.datetime(2024, 6, 1),
    tags=["homework"],
    catchup=False
)

# with 블록을 사용하여 DAG context를 설정
with my_dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
