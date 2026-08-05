# 🚀 Python Azure SRE Demo App

This project demonstrates a **simple SRE (Site Reliability Engineering) workflow** using:

* Flask application (simulated failures)
* Azure Application Insights (logging & monitoring)
* AI-based SRE Agent

---

## 🧠 Overview

This application simulates real-world production issues like:

* High CPU usage
* Random application failures

Logs are sent to Azure Application Insights, where alerts can be configured to trigger automated SRE workflows.

---

## 🏗️ Architecture

```
Flask App → Application Insights → Alerts → SRE Agent
```

---

## ⚙️ Prerequisites

* Python 3.10+ (3.11 recommended)
* Azure Application Insights resource
* Connection string from Azure

---

## 📦 Installation

```bash
uv pip install flask psutil opencensus-ext-azure opencensus-ext-flask
```

---

## 🔑 Configuration

Update your Application Insights connection string:

```python
connection_string = "YOUR_CONNECTION_STRING"
```

---

## 🧑‍💻 Application Code

```python
from flask import Flask, jsonify
import random
import psutil
import logging
import threading
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware

app = Flask(__name__)

connection_string = "YOUR_CONNECTION_STRING"

# Application Insights Middleware
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string=connection_string)
)

# Logging setup
logger = logging.getLogger(__name__)
handler = AzureLogHandler(connection_string=connection_string)
handler.lock = threading.RLock()  # Fix for Python 3.13
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@app.route("/")
def home():
    logger.info("Home endpoint hit")
    return "App is running"

@app.route("/health")
def health():
    cpu = psutil.cpu_percent(interval=1)

    logger.info(f"Health check | CPU: {cpu}")

    if cpu > 80 or random.choice([True, False]):
        logger.error(f"App DOWN | CPU: {cpu}")
        return jsonify({"status": "DOWN", "cpu": cpu}), 500

    return jsonify({"status": "UP", "cpu": cpu})

@app.route("/load")
def load():
    logger.warning("Generating CPU load")

    for _ in range(10**7):
        pass

    return "Load generated"

if __name__ == "__main__":
    app.run(port=5000)
```

---

## ▶️ Running the Application

```bash
python app.py
```

---

## 🧪 Testing Endpoints

### Home

```
GET /
```

### Health Check

```
GET /health
```

### Simulate Load

```
GET /load
```

---

## 📊 Viewing Logs in Azure

Go to **Application Insights → Logs**

Run query:

```kusto
traces
| order by timestamp desc
```

---

## 🚨 Create Alert for Failures

Use this query:

```kusto
traces
| where message contains "App DOWN"
```

Set alert:

* Threshold: > 0
* Frequency: 1 minute

---

## 🔄 SRE Workflow

1. App generates failure
2. Logs sent to Azure
3. Alert triggered
4. SRE agent detects issue
5. Auto-healing action triggered (optional)

---

## 🧠 Key Learning

This project demonstrates how to:

* Simulate failures in an application
* Send telemetry to Azure
* Create alert-based SRE workflows
* Build foundation for AI-driven operations

---

## 👨‍💻 Author

Rohit K Singh
DevOps / SRE / Azure Enthusiast
