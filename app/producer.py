import pika
import json
import os

class Producer():
    # Establish a connection with RabbitMQ server.
    url = os.environ['CLOUDAMQP_URL']
    params = pika.URLParameters(url)
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
            cls.connection = pika.BlockingConnection(cls.params)
            cls.channel = cls.connection.channel()
        except pika.exceptions.ChannelClosed:
            cls.channel = cls.connection.channel()
