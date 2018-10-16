import pika
import json
import os
import time

url = os.environ.get('amqp://dkwttbup:6l_JoEG8FQQNFR-Imf-FWzs8H2avSPhe@lion.rmq.cloudamqp.com/dkwttbup', 'rabbitmq')
time.sleep(10)
#params = pika.URLParameters(url)
local = pika.ConnectionParameters('rabbitmq')
connection = pika.BlockingConnection(local)
channel = connection.channel()
# Create a queue to which the message will be delivered.
channel.queue_declare(queue='Helge-api-posts')
print(" [*] Producer is ready")


# Using connection, posting to 'Helge-api-posts', serialized as JSON
def post_to_queue(message):
    channel.basic_publish(exchange='',
                          routing_key='Helge-api-posts',
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                             delivery_mode=2,  # make message persistent
                          ))
