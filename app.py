from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    })

@app.route("/")
def home():
    return jsonify({"status": "CloudPlatform API is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
