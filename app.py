from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
#tets
app = Flask(__name__)

# This will be our counter for the index route
REQUESTS = Counter('index_requests_total', 'Times the index route has been visited')

@app.route('/')
def index():
    REQUESTS.inc()  # Increment the counter
    return "Hello, World!"

@app.route('/metrics')
def metrics():
    # We'll generate the latest metrics and return them as a plaintext response
    # Prometheus will be able to scrape this
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
