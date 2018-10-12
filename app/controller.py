import database
import datetime
from bson.json_util import dumps
import pymongo
import json
import rabbitmq_consumer

# Global variables
db_con = database.get_db_conn()


# Getting the latest created object in mongodb using timestamp function in objectid
def get_latest_id():
    posts = db_con.posts
    item = posts.find_one(sort=[('_id', pymongo.DESCENDING)])
    return int(item["hanesst_id"])


# Formatting and inserting the message from rabbit into database
def add_post(message):
    posts = db_con.posts
    data = json.loads(message)
    posts.insert_one(data)
    print("object inserted")

def prepare():
	rabbitmq_consumer.start()