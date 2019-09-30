#!/bin/bash
# description: I'm so handsome
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8001
#nohup python manage.py runserver 0.0.0.0:8001 >> /code/SH_backend/logs/backend.log 2>&1 &
##启动celery
#celery -A spic_backend.mycelery worker -l info >> /code/SH_backend/logs/celery_server.log 2>&1 &
##启动kafka监听程序
#python script_kafka/task_recv_consumer.py >> /code/SH_backend/logs/kafka_listen.log 2>&1 &
##socket监听程序
#python script_socket/socket_listen.py >> /code/SH_backend/logs/socket_listen.log 2>&1 &
