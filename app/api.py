from flask import Flask, request

from producer import post_to_queue

"""
API DOCUMENTATION : https://github.com/HackerNews/Helge-api
Python API service running on Flask framework,
connected to a mongodb database.
"""

app = Flask(__name__)


# Status if project is running
@app.route('/status', methods=['GET'])
def status():
    return "Alive"


# Find latest digested post by querying the backend directly on port 5000
@app.route('/latest', methods=['GET'])
def latest():
    return "42"


# Put the posted data directly on the queue
@app.route('/post', methods=['POST'])
def post():
    con = request.json
    post_to_queue(con)
    return "OK", 200


# Run the app on 0.0.0.0:5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
