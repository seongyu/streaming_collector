# describe get mqtt message from client to celery broker

from worker import collect #,app 

import pika
import json
from datetime import datetime

def callback(ch, method, properties, body):
	try :
		print('************** catch request')
		orr = json.loads(body)
		ks = orr.keys()
		for k in ks :
			if k not in ('eui','timestamp') :
				typ = k
		nrr = {
		'eui':orr['eui'],
		'tms':orr['timestamp'],
		'typ':typ,
		'msg':orr[typ]
		}
		collect.delay(nrr)
	except Exception as err :
		print(err)
		pass

def connection_set():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5671))
	channel = connection.channel()
	channel.queue_declare(queue='lora')

	channel.basic_get(callback,queue='lora')

	print('Interface activated. To exit press CTRL+C')
	channel.start_consuming()

if __name__=='__main__':
	# app.start()
	connection_set()
