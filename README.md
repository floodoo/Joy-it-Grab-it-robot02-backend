# Joy-it-Grab-it-robot02-backend
The backend for the [Joy-it-Grab-it-robot02](https://joy-it.net/en/products/Robot02) robot arm. You can use it with my [Flutter app](https://github.com/floodoo/Joy-it-Grab-it-robot02-frontend).

## Installation
Install the backend on your raspberry pi with the [MOTOPI](https://joy-it.net/en/products/RB-Moto3) board.
### Install dependencies
`sudo pip3 install -r requirements/requirements.txt`
## Configuration
### Edit servo settings
```json
"0": {
    "id": 0,
    "pwm_min": 600,
    "pwm_max": 2400,
    "pwm_neutral": 1500,
    "pos_min": -1000,
    "pos_max": 1000,
    "pos_neutral": 0
},
```
#### Position values
pos_min, pos_max and pos_neutral are the values for the frontend sliders. If you edit these values, you need to edit the slider values in the [frontend](https://github.com/floodoo/Joy-it-Grab-it-robot02-frontend/blob/b8bc27be15e0c590dce074ef678c046d23221934/lib/ui/screens/home/widgets/control_slider.dart#L87) too.

#### PWM values
pwm_min, pwm_max and pwm_neutral are the values for the servos. Change these values so that the servos only move so far that nothing is giong to break.
### Add API endpoint to the frontend
After you run the `main.py`, you can see the API endpoint in your terminal:
```bash
* Serving Flask app 'app.robot' (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on all addresses.
  WARNING: This is a development server. Do not use it in a production deployment.
* Running on http://xxx.xxx.xxx.xx:5000/ (Press CTRL+C to quit)
```
Then you have to add the API endpoint to the [app](https://github.com/floodoo/Joy-it-Grab-it-robot02-frontend#select-your-api-endpoint).