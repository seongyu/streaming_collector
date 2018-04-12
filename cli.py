import pika
import json
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5671))
channel = connection.channel()

message = arr = {'eui':'test',"timestamp":"2017-08-11T07:42:51.081853Z","stat":{
	"time":"2017-08-11T07:42:51.081853Z",
	"lati":37.49290,
	"long":127.01302,
	"alti":30,
	"rxnb":1,
	"rxok":1,
	"rxfw":1,
	"ackr":100.0,
	"dwnb":1,
	"txnb":1,
	"pfrm":"MultiTech",
	"mail":"hoonbpark@gmail.com",
	"desc":"Data Alliance - MultiTech Gateway"
}}

channel.queue_declare(queue='lora')

channel.basic_publish(exchange='',
	routing_key='lora',
	body=json.dumps(message))
connection.close()