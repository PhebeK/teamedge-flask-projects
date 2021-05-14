from flask_apscheduler import APScheduler
from flask import Flask, render_template, redirect, url_for, request
from datetime import date
import requests
from sense_hat import SenseHat  
from time import sleep
import sqlite3

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/main')
def main():
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    store = []
    rows = curs.execute("SELECT * from store")
    for row in rows:
        message = {'task': row[1], 'date':row[2], 'rowid': row[0]}
        print(message)
        store.append(message)
    conn.close()
    return render_template('mytask.html', mytask = store)

@app.route('/task')
def task():
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    store = []
    rows = curs.execute("SELECT * from store")
    for row in rows:
        message = {'task': row[1], 'date':row[2], 'rowid': row[0]}
        print(message)
        store.append(message)
    conn.close()
    return render_template('mytask.html', mytask = store)

@app.route('/success', methods=['POST'])
def success():
    task = request.form['task']
    date = request.form['date']
    print(task)
    print(date)
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO store (task,date) VALUES((?),(?))",(task,date))
    conn.commit()
    conn.close()
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    store = []
    rows = curs.execute("SELECT * from store")
    for row in rows:
        message = {'task': row[1], 'date':row[2]}
        print(message)
        store.append(message)
    conn.close()
    return render_template('store.html', task=task, date=date, mytask = store)


@app.route('/sent', methods=['POST'])
def sent():
    task = request.form['task']
    date = request.form['dt']
    print(task)
    print(date)
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO store (task,date) VALUES((?),(?))",(task,date))
    conn.commit()
    conn.close()

    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    store = []
    rows = curs.execute("SELECT * from store")
    for row in rows:
        message = {'task': row[1], 'date':row[2], 'rowid': row[0]}
        print(message)
        store.append(message)
    conn.close()
    return render_template('mytask.html', task=task, date=date, mytask = store)



@app.route('/all')
def all():
     conn = sqlite3.connect('./static/data/store.db')
     curs = conn.cursor()
     mytask = []
     rows = curs.execute("SELECT * from store")
     for row in rows:
         message = {'task': row[1], 'date':row[2], 'rowid': row[0]}
         print(message)
         storeappend(message)
     conn.close()
     return render_template('mytask.html', mytask = store)


@app.route('/delete/<rowid>')
def delete(rowid): 
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM store WHERE rowid="+rowid)
    
    print(rowid)
    conn.commit()
    conn.close()

    #scheduler.remove_job(rowid)
    return redirect(url_for('main'))



@app.route('/edit/<rowid>')
def edit(rowid):
    conn = sqlite3.connect('./static/data/store.db')
    curs = conn.cursor()
    curs.execute("UPDATE store SET  WHERE rowid="+rowid)
    
    print(rowid)
    conn.commit()
    conn.close()
  
    return redirect(url_for('main'))


if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')