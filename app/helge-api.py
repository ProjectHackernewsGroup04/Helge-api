from flask import Flask, request
import rabbitmq_producer
import requests

"""
API DOCUMENTATION : https://github.com/HackerNews/Helge-api
Python API service running on Flask framework,
connected to a mongodb database.
"""

app = Flask(__name__)




# Status checking if application is running
# Alive if 200
# Updating if updating process is ongoing
# Down if 400-500
@app.route('/status', methods=['GET'])
def status():
    r = requests.get("http://backend-app:5000/helge-api/status")
    return r.content

# Find latest digested post by querying the backend directly on port 5000
@app.route('/latest', methods=['GET'])
def latest():
    r = requests.get("http://backend-app:5000/helge-api/latest")
    return r.content

# Put the posted data directly on the queue
@app.route('/post', methods=['POST'])
def post():
    con = request.json
    rabbitmq_producer.post_to_queue(con)
    return "OK", 200


# Run the app on 0.0.0.0:5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


