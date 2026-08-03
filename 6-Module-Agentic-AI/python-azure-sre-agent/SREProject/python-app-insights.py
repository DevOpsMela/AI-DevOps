from flask import Flask, jsonify
import random
import psutil
import logging
import threading
from opencensus.ext.azure.log_exporter import AzureLogHandler

# Azure App Insights
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware

app = Flask(__name__)

# ✅ Your connection string
connection_string = "InstrumentationKey=fb5bfc0b-0b6b-4381-8681-acf626b75b86;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/;ApplicationId=fd802a8e-21e1-420e-baef-69367967dc28"

# ✅ FIX: Use exporter (not exporter_options)
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string=connection_string)
)

# ✅ Logging setup
# logger = logging.getLogger(__name__)
# logger.addHandler(AzureLogHandler(connection_string=connection_string))
# logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
handler = AzureLogHandler(connection_string=connection_string)

# 🔥 Important fix
handler.lock = threading.RLock()

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
        return jsonify({
            "status": "DOWN",
            "cpu": cpu
        }), 500

    return jsonify({
        "status": "UP",
        "cpu": cpu
    })


@app.route("/load")
def load():
    logger.warning("Generating CPU load")

    for _ in range(10**7):
        pass

    return "Load generated"


if __name__ == "__main__":
    app.run(port=5000)