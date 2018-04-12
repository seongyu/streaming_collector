from streaming.util import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from cassandra.cqlengine import management
from importlib import import_module
from pyclbr import readmodule
from streaming import setting
from streaming.data.cassandra.connection import *

import os.path

def sync_table(keyspace):
	logger.debug('Table synchronization start ***')
	models = readmodule('model',[os.path.join(setting.CASSANDRA_DB_PATH, keyspace)])
	models.pop('Model',None)

	module_root = os.path.join(
		os.path.basename(setting.ROOT_PATH),
		os.path.relpath(setting.CASSANDRA_DB_PATH,setting.ROOT_PATH)
		).replace('/','.')+'.'

	register_connection()

	for model in models.keys():
		management.sync_table(
			getattr(import_module(module_root+keyspace+'.models'),model),
			keyspaces = [keyspace_DTP(keyspace)],
			connections = [setting.MY_NETWORK]
		)
	unregister_connection()
	logger.debug('*** Synchronized successfully')