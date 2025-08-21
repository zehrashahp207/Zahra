from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {'id': 1, 'task': 'Kitab oxu'},
    {'id': 2, 'task': 'Kod yaz'},
    {'id': 3, 'task': 'Zehra'}
]

@app.route('/tasks', methods=['GET'])
def show_tasks():
    return jsonify(tasks)

@app.route('/taks', methods=['POST'])
def add_task():
    new_task = request.json.get('task')
    if not new_task:
        return {"error": "Task metnini gonderin"}, 400
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    task = {'id': new_id, 'task': new_task}
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return {"error": "Task tapılmadı"}, 404
    new_task_text = request.json.get('task')
    if not new_task_text:
        return {"error": "Task metnini gonderin"}, 400
    task['task'] = new_task_text
    return jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)