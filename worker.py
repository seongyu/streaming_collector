#describe from celery worker to cassandra cluster

from streaming import setting
from streaming.data.cassandra import connection
from streaming.data.cassandra.db.lora_streaming.models import Store00

from celery import Celery
from datetime import datetime
import uuid
import json

app = Celery('tasks',
	broker = setting.COLLECTOR_CELERY_BROKER_URLS[setting.MY_NETWORK],
	enable_utc = True,
	timezone = 'UTC',
	)


@app.task
def collect(arr):
	connection.setup('lora_streaming')
	Store00.create(
		uid = uuid.uuid1(),
		eui = arr['eui'],
		tms = datetime.strptime(arr['tms'], "%Y-%m-%dT%H:%M:%S.%fZ"),
		typ = arr['typ'],
		msg = json.dumps(arr['msg'])
		)