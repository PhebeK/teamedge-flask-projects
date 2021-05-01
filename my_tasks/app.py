from flask import Flask, render_template, request, current_app as app
from flask_apscheduler import APScheduler
import sqlite3


app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def reminder():
    return render_template('tasks.html')


@app.route('/task', methods=['GET', 'POST'])
def form():
    form = request.form['task']
    date = request.form['calendar']
    return render_template('tasks.html', task = form)


@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    store = []
    rows = curs.execute("SELECT * from store")
    return render_template('tasks.html', store = store)


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')