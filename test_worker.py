from celery import Celery


from cassandra.cqlengine import connection
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from datetime import datetime
import uuid


class Store00(Model):
	uid = columns.UUID(primary_key=True)
	eui = columns.Text(required=True)
	tms = columns.DateTime(primary_key=True)
	typ = columns.Text(required=True)
	msg = columns.Text(required=False)

def setup():
	print('127.0.0.1','lora_streaming')
	connection.setup(['127.0.0.1'],'lora_streaming')


def register_connection():
	connection.register_connection(['127.0.0.1'],'lora_streaming')



app = Celery('tasks',
	broker = ['amqp://guest:guest@localhost:5672//'],
	enable_utc = True,
	timezone = 'UTC',
	)


@app.task
def collect():
	setup()
	uid = uuid.uuid1()
	eui = 'test'
	typ = 'test type'
	tms = datetime.now()
	msg = 'sample test import'

	print('inserted ... . .')

	Store00.create(
		uid = uid,
		eui = eui,
		typ = typ,
		tms = tms,
		msg = msg
		)


if __name__ == '__main__':
	app.start()