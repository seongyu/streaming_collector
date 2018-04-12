import pika,json,pytz

arr = {'eui':'test',"timestamp":"2017-08-23T07:42:51.081853Z",'test':''}


credentials = pika.PlainCredentials('leon','leon')
conn_config = pika.ConnectionParameters(host='localhost', port=5672,credentials=credentials)

def loop(i):
	connection = pika.BlockingConnection(conn_config)
	channel = connection.channel()

	channel.exchange_declare(exchange='acc', exchange_type='fanout')

	# for test code ....

	channel.basic_publish(exchange='acc',routing_key="",body=json.dumps(arr))
	connection.close()
	print('send message =====> ', arr)

if __name__=='__main__':
	for i in range(1):
		loop(i)