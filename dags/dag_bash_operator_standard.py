from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

my_dag = DAG(
    dag_id="dags_bash_operator_standard",
    schedule="0 9 * * 1,5"
    start_date=datetime.datetime(2024, 6, 1),
    tags=["homework"],
    catchup=False
)

bash_t1 = BashOperator(
    task_id="bash_t1",
    dag=my_dag,
    bash_command="echo whoami",
)

bash_t2 = BashOperator(
    task_id="bash_t2",
    dag=my_dag,
    bash_command="echo $HOSTNAME",
)

bash_t1 >> bash_t2
