from flask import Flask,render_template,jsonify,request
import requests

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def fetchWeather():
    data = request.get_json()
    city = data.get("city") 

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        weather_data = response.json()
        current = weather_data['current_condition'][0]
        return jsonify({
            "city": city.title(),
            "temperature_C": current['temp_C'],
            "feels_like_C": current['FeelsLikeC'],
            "condition": current['weatherDesc'][0]['value'],
            "wind_kph": current['windspeedKmph']
        })
    except Exception as e:
        return jsonify({"error": "Weather fetch failed", "details": str(e)}), 500


if __name__=="__main__":
    app.run(debug=True)