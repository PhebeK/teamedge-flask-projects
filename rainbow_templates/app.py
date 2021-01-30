from flask import Flask, render_template, current_app as app

app = Flask(__name__)


@app.route('/red')
def red():
    return render_template('rainbow.html',color='red')

@app.route('/orange')
def orange():
    return render_template('rainbow.html',color='orange')

@app.route('/yellow')
def yellow():
    return render_template('rainbow.html',color='yellow')

@app.route('/green')
def green():
    return render_template('rainbow.html',color='green')

@app.route('/blue')
def blue():
    return render_template('rainbow.html',color='blue')

@app.route('/indigo')
def indigo():
    return render_template('rainbow.html',color='indigo')

@app.route('/violet')
def violet():
    return render_template('rainbow.html',color='violet')

@app.route('/rainbow')
def rainbow():
    colors =['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('rainbow.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')