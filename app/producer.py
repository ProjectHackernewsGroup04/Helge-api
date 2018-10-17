import pika
import json
import os
# Establish a connection with RabbitMQ server.
url = os.environ['CLOUDAMQP_URL']
print(url)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()


# Using connection, posting to 'Helge-api-posts', serialized as JSON
def post_to_queue(message):
    # Create a queue to which the message will be delivered.
    channel.queue_declare(queue='helge-api-posts')
    channel.basic_publish(exchange='', routing_key='helge-api-posts', body=json.dumps(message),
                          properties=pika.BasicProperties(
                              content_type='text/plain',
                              delivery_mode=2,  # make message persistent
                          ))
