# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_user = request.form['user']
    task_name = request.form['name']
    task_time = request.form['time']
    task_description = request.form['description']
    if task_user == "" or task_name == "" or task_time == "" or task_description == "":
        return redirect(url_for('index'))
    else:
        tasks[task_name] = {'user':task_user, 'time': task_time, 'description': task_description}
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
