from flask import Flask, request, jsonify

from producer import Producer
import requests
import os
import sys

from prometheus_client import start_http_server, Summary, Counter, Gauge, generate_latest, REGISTRY, Histogram

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# A counter to count the total number of HTTP requests
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])

# A gauge (i.e. goes up and down) to monitor the total number of in progress requests
IN_PROGRESS = Gauge('http_requests_inprogress', 'Number of in progress HTTP requests')

# A histogram to measure the latency of the HTTP requests
TIMINGS = Histogram('http_request_duration_seconds', 'HTTP request latency (seconds)')

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
@IN_PROGRESS.track_inprogress()
@TIMINGS.time()
def post():
    try:
        con = request.json
        con['auth'] = request.headers['Authorization']
        Producer.post_to_queue(con)
        REQUESTS.labels(method='POST', endpoint="/post", status_code=200).inc()
        return "OK", 200
    except:
        REQUESTS.labels(method='POST', endpoint="/post", status_code=400).inc()
        return "ERROR", 400


@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(REGISTRY)

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

# Run the app on 0.0.0.0:5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
