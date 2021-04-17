from flask import Flask, render_template, request, current_app as app
from sense_emu import SenseHat
import sqlite3

app = Flask(__name__)
sense = SenseHat()


@app.route('/')
def index():
    return render_template("message.html")


@app.route('/done', methods=['GET', 'POST'])
def done():
    message = request.form['message']
    sense.show_message(message)
    
    return render_template('done.html', message = message)


@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    bulletin = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        lines = {'message': row[0]}
        bulletin.append(lines)
    conn.close
    return render_template('all.html', bulletin = bulletin)
    

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
