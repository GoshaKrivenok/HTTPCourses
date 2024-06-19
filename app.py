from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'f7802b76e87178153fc230d820079cc4'  


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return "City parameter is required", 400

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200
    elif response.status_code == 401:
        return "Unauthorized", 401
    elif response.status_code == 404:
        return "City not found", 404
    else:
        return "Internal Server Error", 500


if __name__ == '__main__':
    app.run(debug=True)