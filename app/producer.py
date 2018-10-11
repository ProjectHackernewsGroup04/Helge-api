import pika
import json
# Establish a connection with RabbitMQ server.
url = 'amqp://pgkettyz:PIjFclgL5aB8c0ZP4OwWUZZ3DbgKEriY@raven.rmq.cloudamqp.com/pgkettyz'
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
