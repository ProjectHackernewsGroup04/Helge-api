from flask import Flask
from bson.json_util import dumps

# API DOCUMENTATION : https://github.com/HackerNews/API
# Python API service running on Flask framework,
# connected to a mongodb database.

# Global variables
app = Flask(__name__)


# Temporally homepage
@app.route('/status', methods=['GET'])
def status():
    return "It's alive"


# Get all stories
@app.route('/latest', methods=['GET'])
def latest():
    # Find latest digested post by querying the backend directly on port 5000
    return "42"

# Get item by id
@app.route('/post', methods=['POST'])
def post(post_id):
    # Put the posted data directly on the queue
    return "Some kewl data"


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# Run the app on 0.0.0.0:5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
