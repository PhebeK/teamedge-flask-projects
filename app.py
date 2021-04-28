from flask_apscheduler import APScheduler
from flask import Flask, render_template, request, current_app as current_app
import sqlite3

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def done():
    task = request.form['task']


    return render_template('tasks.html', task = task )
