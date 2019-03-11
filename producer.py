import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='world')

channel.basic_publish(
  exchange='',
  routing_key='world',
  body='{ \"symbol\" : \"LEX\" }')

print(" [x] Message Sent")

connection.close()
