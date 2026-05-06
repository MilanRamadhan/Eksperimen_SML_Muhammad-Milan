from flask import Flask, Response
import requests
import time
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter("request_count_total", "Total request ke model")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Waktu response model")

# ⚠️ GANTI localhost → host.docker.internal (biar bisa dari Docker)
MODEL_URL = "http://127.0.0.1:5001/invocations"

def call_model():
    data = {
        "dataframe_split": {
            "columns": ["age", "fare", "sex", "sibsp", "parch", "pclass", "embarked"],
            "data": [[22.0, 7.25, 1.0, 1.0, 0.0, 3.0, 0.0]]
        }
    }

    start = time.time()
    res = requests.post(MODEL_URL, json=data)
    latency = time.time() - start

    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(latency)

    return res.json()

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

@app.route("/test")
def test():
    result = call_model()
    return result

if __name__ == "__main__":
    # 🔥 WAJIB: ganti ke 0.0.0.0 biar bisa diakses Docker
    app.run(host="0.0.0.0", port=8000)