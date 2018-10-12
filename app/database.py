from pymongo import MongoClient

# Database names
client = MongoClient('database', 27017)
db_name = "hackernews"
collection_name_posts = "posts"


# Get the connection instance
def get_db_conn():
    connection = client[db_name]
    return connection

