# Bike sharing prediction model - Adilet Gaparov

## Usage

Before running the Flask application, you will need to install the library ie_bike_model by running the command below in the directory of the application:

```
$ pip install .
```

To test the library, you can run the following code:

```python
>>> import datetime as dt
>>> from ie_bike_model.model import train_and_persist, predict
>>> train_and_persist()
>>> predict({
...     "date": dt.datetime(2011, 1, 1, 0, 0, 0),
...     "weathersit": 1,
...     "temperature_C": 9.84,
...     "feeling_temperature_C": 14.395,
...     "humidity": 81.0,
...     "windspeed": 0.0,
... })
24
```

To run the app:

```
$ flask run
```

To verify that Flask runs correctly, enter the following URL in the browser:

```
http://localhost:5000/
```

that should show "Hello, World!" message. The main route accepts parameter "name" that will replace "World". For example, the following code will print "Hello, Adilet!":

```
http://localhost:5000/?name=Adilet
```

To check the R-squared scores of Ridge and XGBoost models on training set:

```
http://localhost:5000/train
```

To get the predictions for default parameters:

```
http://localhost:5000/predict
```

The API accepts the following parameters:
* date: date in ISO format (YYYY-MM-DD)
* weathersit: category of weather (1,2,3,4)

(1) Clear, Few clouds, Partly cloudy, Partly cloudy;
(2) Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist;
(3) Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds;
(4) Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog;

* temperature_C: temperature in Celsius
* feeling_temperature_C: feeling temperature in Celsius
* humidity: humidity level
* windspeed: wind speed in m/s

When _date_ is not given, the API takes **tomorrow**. When _weathersit_ is not given, the API takes the **median** value for the given month from the training set. If other parameters are not given, the API takes the **mean** value for the given month.  

## Development

To install a development version of the library:

```
$ flit install --symlink --extras=dev
```

To run the tests:

```
$ pytest
```

To measure the coverage:

```
$ pytest --cov=ie_bike_model
```
