from flask import Flask, request, jsonify

from producer import Producer
import requests
import os
import sys

"""
API DOCUMENTATION : https://github.com/HackerNews/Helge-api
Python API service running on Flask framework,
connected to a mongodb database.
"""

app = Flask(__name__)

backend_url = os.environ['BACKEND_URL']

# Status if project is running
@app.route('/status', methods=['GET'])
def status():
    r = requests.get(backend_url + "/status")
    json = r.json()
    if 'status' in json:
        return json['status']
    else:
        return 'Down'


# Find latest digested post by querying the backend directly on port 5000
@app.route('/latest', methods=['GET'])
def latest():
    r = requests.get(backend_url + "/latest")
    json = r.json()
    if 'post' in json:
        return json['post']['id']
    return None


# Put the posted data directly on the queue
@app.route('/post', methods=['POST'])
def post():
    con = request.json
    con['auth'] = request.headers['Authorization']
    Producer.post_to_queue(con)
    return "OK", 200


# Run the app on 0.0.0.0:5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
