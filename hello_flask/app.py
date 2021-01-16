from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests


app = Flask(__name__)

@app.route('/')
def index():
    vacay = [ 'Venice, Italy' , 'Bora Bora' , 'Santorini' , 'Paris, France' , 'Iceland' ]
    return render_template('index.html', greeting= 'Hello',  name= "Phebe", vacay=vacay, description='This is my website :)')
    
@app.route('/nasa')
def show_nasa_pic():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)

    data = response.json()

    return render_template('nasa.html',data = data)
    

@app.route('/api/v1/album', methods=['GET'])
def album_json():
    album_info = os.path.join(app.static_folder, 'data', 'album.json')
    with open(album_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)

@app.route('/api/v1/movies', methods=['GET'])
def movies_json():
    movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




