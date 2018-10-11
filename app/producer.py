import pika
import json
import os
# Establish a connection with RabbitMQ server.
url = 'amqp://dkwttbup:6l_JoEG8FQQNFR-Imf-FWzs8H2avSPhe@lion.rmq.cloudamqp.com/dkwttbup'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Create a queue to which the message will be delivered.
channel.queue_declare(queue='Helge-api-posts')


# Using connection, posting to 'Helge-api-posts', serialized as JSON
def post_to_queue(message):
    channel.basic_publish(exchange='',
                          routing_key='Helge-api-posts',
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                             delivery_mode=2,  # make message persistent
                          ))
