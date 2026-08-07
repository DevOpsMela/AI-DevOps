from flask import Flask, jsonify
import random
import time
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running"

@app.route("/health")
def health():
    cpu = psutil.cpu_percent(interval=1)
    
    # Simulate failure
    if cpu > 80 or random.choice([True, False]):
        return jsonify({
            "status": "DOWN",
            "cpu": cpu,
            "error": "High CPU or random failure"
        }), 500

    return jsonify({
        "status": "UP",
        "cpu": cpu
    })

@app.route("/load")
def load():
    # Simulate CPU spike
    for _ in range(10**7):
        pass
    return "Load generated"

if __name__ == "__main__":
    app.run(port=5000)