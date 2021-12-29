# Joy-it-Grab-it-robot02-backend
## Installation
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
pos_min, pos_max and pos_neutral are the values for the frontend sliders. If you edit these values, you need to edit the slider values in the [frontend](https://github.com/floodoo/Joy-it-Grab-it-robot02-frontend/blob/main/lib/ui/screens/home/widgets/control_slider.dart) too.

These values are used to [calculate](https://github.com/floodoo/Joy-it-Grab-it-robot02-backend/blob/52e37b3f714cf3ee46a6bbfe17592b7ebe7a8922/app/servo.py#L99) the pwm values for the servos.

#### PWM values
pwm_min, pwm_max and pwm_neutral are the values for the servos. Change these values so that the servos only move so far that nothing is giong to break.
### Add API endpoint to the frontend
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

Add the showing API endpoint to the frontend. [Here](https://github.com/floodoo/Joy-it-Grab-it-robot02-frontend#select-your-api-endpoint) you can read how to do that.