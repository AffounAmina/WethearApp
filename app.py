from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    country = request.form['country']
    api_key = 'e2870239ea3300f0fb99d6cdff21c5d4'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        return render_template('index.html', weather=weather)
    else:
        error_message = "Country not found. Please try again."
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)