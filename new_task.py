import sys
import pika

message=' '.join(sys.argv[1:]) or 'Hello World!'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.basic_publish(exchange='',
                     routing_key='hello',
                     body=message)

print(" [x] Sent %r" % message)