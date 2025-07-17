from asyncio import tasks
from flask import Flask, request, jsonify   # type: ignore

app = Flask(__name__)

task = []

@app.route('/tasks', metods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', metods=['POST'])
def get_tasks():
    task = request.get_json()
    tasks.append(task)
    return jsonify(task),200
if __name__ == '__main__':
    app.run()