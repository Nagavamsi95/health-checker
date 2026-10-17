from flask import Flask, jsonify
from checker import run_checks

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/status")
def status():
    results = run_checks()
    overall = "UP" if all(r["status"] == "UP" for r in results) else "DOWN"
    return jsonify(overall=overall, services=results), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)