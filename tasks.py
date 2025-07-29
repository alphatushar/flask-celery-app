import time
from celery import Celery
import os

RABBIT_HOST = os.getenv("RABBIT_HOST", "rabbitmq")

celery = Celery(
    'tasks',
    broker=f'amqp://guest:guest@{RABBIT_HOST}//',
    backend='rpc://'
)

@celery.task
def create_task(name):
    print(f"📥 Received task: {name}")
    time.sleep(5)
    print(f"✅ Task completed: {name}")
    return f"Task {name} completed"