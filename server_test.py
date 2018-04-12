# pika.credentials.PlainCredentials('acd', '1234', erase_on_connect=False)
import pika,sys,json,future,pprofile

def sendJson(json):
	connection = pika.BlokingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='mqtt',durable=True)
	channel.queue_bind(exchange='mqtt_exchange',queue='mqtt')
	channel.basic_publish(exchange='mqtt_exchange',routing_key='topic.test',body=json)
	connection.close()