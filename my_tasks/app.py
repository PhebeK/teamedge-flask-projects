from flask_apscheduler import APScheduler
from flask import Flask, render_template, request, current_app as app
import sqlite3

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def done():
    message = request.form['message']

    
    return render_template('index.html', message = message)













if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')