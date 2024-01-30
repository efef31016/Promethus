#!/bin/bash
AI_SYS_PATH=/srv/ai-airflow/dags/alert/app
VENV_PATH=$AI_SYS_PATH/venv
echo "AI SYS PATH: $AI_SYS_PATH"
mkdir -p $AI_SYS_PATH/service_log

while true
do
    . $VENV_PATH/bin/activate
    date >> $AI_SYS_PATH/service_log/service.log
    python $AI_SYS_PATH/main.py >> $AI_SYS_PATH/service_log/service.log
    sleep 3
done

