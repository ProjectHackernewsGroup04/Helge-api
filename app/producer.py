import pika
import json
import os
import time

url = os.environ['CLOUDAMQP_URL']
params = pika.URLParameters(url)
connection = None

try:
    connection = pika.BlockingConnection(params)
except pika.exceptions.ConnectionClosed:
    time.sleep(5)
    connection = pika.BlockingConnection(params)

channel = connection.channel()

tries = 5
for i in range(tries):
    try:
        etablish_connection()
    except Exception as e:
        time.sleep(5)
        continue


def etablish_connection():
    channel.queue_declare(queue='helge-api-posts', durable=True)


class Producer():
    # Establish a connection with RabbitMQ server.
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    # Using connection, posting to 'Helge-api-posts', serialized as JSON
    @classmethod
    def post_to_queue(cls, message):
        try:
        # Create a queue to which the message will be delivered.
            cls.channel.queue_declare(queue='helge-api-posts', durable=True)
            cls.channel.basic_publish(exchange='', routing_key='helge-api-posts', body=json.dumps(message),
                                  properties=pika.BasicProperties(
                                      content_type='application/json',
                                      delivery_mode=2,  # make message persistent
                                  ))
        except pika.exceptions.ConnectionClosed:
            cls.connection = pika.BlockingConnection(params)
            cls.channel = cls.connection.channel()
        except pika.exceptions.ChannelClosed:
            cls.channel = cls.connection.channel()
