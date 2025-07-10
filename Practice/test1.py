# from flask import Flask,jsonify
# import requests
# from flask_cors import CORS

# app=Flask(__name__)
# # CORS(app)




# @app.route("/weather",methods=["GET"])
# def index():
#     city='srinagar'
#     API="https://wttr.in/"
#     resp=requests.get(f"{API}{city}?format=j1")
#     if resp.status_code==200:
#         data=resp.json()

#         current = data['current_condition'][0]

#         result = {
#             "city": city,
#             "temperature_C": current['temp_C'],
#             "feels_like_C": current['FeelsLikeC'],
#             "condition": current['weatherDesc'][0]['value'],
#             "wind_kph": current['windspeedKmph']
#         }
#         return jsonify(result)
#     else:
#         print("Error fetching API")
    


# if __name__=="__main__":
#     app.run(debug=True)