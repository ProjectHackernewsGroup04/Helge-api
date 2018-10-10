_This repository is a proxy api for sending tree requests: `/latest`,
`/post` and `/status`. These requests will be going through queue for
load balance using RabbitMQ system._

* Abstract

We install a RabbitMQ server instance on our system.
Then a producer program connects to this server and sends out a message.
RabbitMQ queues that message and sends it off to a consumer program,
that is listening on the RabbitMQ server.

RabbitMQ is a message-oriented middleware system with advanced message
queuing protocol.

[Link to rabbitMQ official](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

* Installing

We added a RabbitMQ server in `Ops/docker-compose.yaml wich is used
in Helge-api and Backend.

* Usage in this project

    * Producer - Helge-api

    * Consumer - Backend-api

