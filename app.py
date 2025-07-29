from flask import Flask, request, jsonify
from tasks import create_task

app = Flask(__name__)

@app.route("/task", methods=["POST"])
def run_task():
    data = request.json
    task = create_task.delay(data.get("name", "default_task"))
    return jsonify({"message": "Task submitted", "task_id": task.id}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)