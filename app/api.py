from flask import Flask

"""
API DOCUMENTATION : https://github.com/HackerNews/Helge-api
Python API service running on Flask framework,
connected to a mongodb database.
"""

app = Flask(__name__)


# Status if project is running
@app.route('/status', methods=['GET'])
def status():
    return "It's alive"


# Find latest digested post by querying the backend directly on port 5000
@app.route('/latest', methods=['GET'])
def latest():
    return "42"


# Put the posted data directly on the queue
@app.route('/post', methods=['POST'])
def post(post_id):
    return "Some kewl data"


# Run the app on 0.0.0.0:5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
