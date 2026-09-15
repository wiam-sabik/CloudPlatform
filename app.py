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
@app.route("/system-status")
def system_status():
    def check(value):
        if value > 90:
            return "critical"
        elif value > 70:
            return "warning"
        else:
            return "ok"

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    checks = {
        "cpu": {"value": cpu, "status": check(cpu)},
        "ram": {"value": ram, "status": check(ram)},
        "disk": {"value": disk, "status": check(disk)}
    }

    statuses = [c["status"] for c in checks.values()]
    if "critical" in statuses:
        overall = "critical"
    elif "warning" in statuses:
        overall = "warning"
    else:
        overall = "ok"

    return jsonify({
        "overall_status": overall,
        "checks": checks
    })

@app.route("/")
def home():
    return jsonify({"status": "CloudPlatform API is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

