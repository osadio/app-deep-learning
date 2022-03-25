import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("draw.html")

@app.route('/perform_prediction', methods=['POST'])
def perform_prediction():
    pixel_array = request.form['pixel_array']
    params = {'pixelarray': pixel_array }
    address = "172.17.0.2"
    port = 8080
    url = f"http://{address}:{port}/predict"
    response = requests.get(url, params=params)
    print(response.text)
    predicted_number = response.text
    return render_template('draw.html', predicted_number=predicted_number, pixel_array=pixel_array)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port)
