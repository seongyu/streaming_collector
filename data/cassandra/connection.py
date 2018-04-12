from streaming.util import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from cassandra.cqlengine import connection
from streaming import setting
from streaming.exception import *
from streaming.util.eval import *

def keyspace_DTP(keyspace):
	eval_setting_DTP()

	if keyspace not in setting.CASSANDRA_KEYSPACES:
		raise UnknownCassandraKeyspace
	return keyspace # It could update if needs DTP process

def register_connection():
	logger.debug('Connecting registration start ***')
	eval_setting_MY_NETWORK()
	connection.register_connection(setting.MY_NETWORK,
		setting.CASSANDRA_CONTACT_POINTS[setting.MY_NETWORK])
	logger.debug('*** Registed successfully')

def setup(keyspace):
	print(setting.CASSANDRA_CONTACT_POINTS[setting.MY_NETWORK],keyspace_DTP(keyspace))
	connection.setup(setting.CASSANDRA_CONTACT_POINTS[setting.MY_NETWORK],
		keyspace_DTP(keyspace))

def unregister_connection():
	logger.debug('Connecting unregistration start ***')
	eval_setting_MY_NETWORK()
	connection.unregister_connection(setting.MY_NETWORK)
	logger.debug('*** Unregisted successfully')