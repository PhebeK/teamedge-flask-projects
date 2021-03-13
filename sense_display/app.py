from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def index():
    return ("Phebe's SenseHat Project")

@app.route('/done')
def done():
    return ("Message sent. Thank you :)")

@app.route('/welcome' ,methods = ['POST','GET'])
def(welcome):
    if request.method == 'POST':
        user = request.form['msg']
        return redirect(url_for('success'))


if __name__ == '__main__':
    app.run(debug = True, host ='0.0.0.0')
