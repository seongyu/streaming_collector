import os.path

DTP = 'D'

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
COLLECTOR_ROOT = os.path.join(ROOT_PATH, 'collector')

NETWORKS = [
	'localhost',
	# 'asia-east1-a',
	# 'us-central1-a',
	]

if DTP != 'D':
	MY_NETWORK = ''
else:	# T or P
	MY_NETWORK = 'localhost'

CASSANDRA_CONTACT_POINTS = {
	'localhost': ['127.0.0.1'],
	# 'asia-east1-a': [
	# 	'10.140.0.2',
	# 	'10.140.0.3',
	# 	'10.140.0.4',
	# 	'10.140.0.5',
	# 	'10.140.0.6',
	# ],
	# 'us-central1-a': [
	# 	'10.128.0.2',
	# 	'10.128.0.3',
	# 	'10.128.0.4',
	# 	'10.128.0.5',
	# 	'10.128.0.6',
	# ],
}

CASSANDRA_DB_PATH = os.path.join(ROOT_PATH, 'data', 'cassandra', 'db')

CASSANDRA_KEYSPACES = [
	'lora_streaming',
]

COLLECTOR_CELERY_BROKER_URLS = {
	'localhost': ['amqp://guest:guest@localhost:5672//'],
	# 'asia-east1-a': [
	# 	'amqp://guest:guest@10.140.0.7:5672//'
	# ],
}

LOG_BACKUP_COUNT = 100
LOG_MAX_BYTES = 10 * 1000 * 1000
LOG_DIR_PATH = os.path.join(ROOT_PATH, 'log')
LOG_FILENAME = 'streaming.log'

