class RabbitMqClient(object):
    __connection = None

    def __init__(self, connection):
        self.__conntection = connection

    @staticmethod
    def post(json_object):
        return "Posted"