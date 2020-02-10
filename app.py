import datetime as dt
from flask import Flask, request

from ie_bike_model.model import predict, train_and_persist
from ie_bike_model.util import read_data

app = Flask(__name__)


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return "Hello, " + name + "!"

@app.route("/train")
def get_train_score():
    
    result = {}
    
    model_list = ['xgboost', 'ridge']
    
    for model in model_list:
        score = train_and_persist(model=model)
        result[model] = score
        
    return result


@app.route("/predict")
def get_predict():
    
    tomorrow = dt.datetime.now() + dt.timedelta(days=1)
    
    hour_original = read_data()
    hour_original =  hour_original[hour_original.mnth==tomorrow.month]
    
    weathersit_avg = hour_original['weathersit'].median()
    temperature_C_avg = hour_original.temp.mean() * 41.0
    feeling_temperature_C_avg = hour_original.atemp.mean() * 50.0
    humiditiy_avg = hour_original.hum.mean() * 100.0
    windspeed_avg = hour_original.windspeed.mean() * 67.0

    
    parameters = dict(request.args)
    parameters["date"] = dt.datetime.fromisoformat(parameters.get("date", tomorrow.isoformat()))
    parameters["weathersit"] = int(parameters.get("weathersit", weathersit_avg))
    parameters["temperature_C"] = float(parameters.get("temperature_C", temperature_C_avg))
    parameters["feeling_temperature_C"] = float(parameters.get("feeling_temperature_C", feeling_temperature_C_avg))
    parameters["humidity"] = float(parameters.get("humidity", humiditiy_avg))
    parameters["windspeed"] = float(parameters.get("windspeed", windspeed_avg))
    
      
    start = dt.datetime.now()

    result = predict(parameters, model=parameters.get('model', 'ridge'))
    
    prediction_time = dt.datetime.now() - start
    
    return {"result": result, "prediction time (seconds)": prediction_time.total_seconds(), "date": parameters['date']}
