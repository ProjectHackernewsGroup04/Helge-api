_This repository is for an api that is receiving three requests: `/latest`,
`/post` and `/status`. The `/post` requests will be going through queue
using RabbitMQ system._

### * Abstract

RabbitMQ is a message-oriented middleware system with advanced message
queuing protocol.

[Link to rabbitMQ official](https://www.rabbitmq.com)

To setup our RabbitMQ queuing protocol, we made an account in CloudAMQP
which are managed RabbitMQ servers in the cloud. Messages are published
to a queue by a producer (`Helge-api/app/producer.py`). Consumers
(Backend) can then get the messages from the queue when the consumer
wants to handle the messages.

Messages can be sent cross languages, platforms and OS, this way of
handling messages, decouple your processes and creates a scalable system.

### * Usage in this project

For starters, we create a CloudAMQP instance by signing up as a customer.
There we assigned `HackerNews` instance which provided us with a url,
that is used in `Helge-api/app/producer.py` for establishing connection
using `pika` (Pika is a pure-Python implementation of the AMQP protocol).

#### * `Helge-api/app/producer.py`:

```python
# Establish a connection with RabbitMQ server.
url = 'amqp://pgkettyz:PIjFclgL5aB8c0ZP4OwWUZZ3DbgKEriY@raven.rmq.cloudamqp.com/pgkettyz'
connection = pika.BlockingConnection(pika.ConnectionParameters(url))
channel = connection.channel()
```

Afterwards we create a queue 'Helge-api-posts' to which the messages
will be delivered.

```python
channel.queue_declare(queue='Helge-api-posts')
```

Then we created a definition that sends POST to 'Helge-api-posts' queue
serialized as a json.dump as we can't send Python types as payload.

```python
def post_to_queue(message):
    channel.basic_publish(exchange='',
                          routing_key='Helge-api-posts',
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                             delivery_mode=2,  # make message persistent
                          ))
```