from flask import Flask,request,render_template,jsonify
import requests


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ipinfo",methods=["GET"])
def getIP():
    url="http://ip-api.com/json"
    resp=requests.get(url)
    if resp.status_code==200:
        data=resp.json()
        return jsonify({
            "ip": data.get("query"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "timezone": data.get("timezone"),
            "latitude": data.get("lat"),
            "longitude": data.get("lon")
        })
    else:
        return jsonify({"error":"Failed to fetch IP"})

if __name__=="__main__":
    app.run(debug=True)