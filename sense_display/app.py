from flask import Flask, render_template, request, current_app as app
from sense_emu import SenseHat

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

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
