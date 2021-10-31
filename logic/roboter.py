from logic.roboterResource import RoboterResource
from flask import Flask
from flask_restful import Api
from logic.servo import Servo


class Roboter():

    DEFAULT_API_BIND_ADDRESS = "0.0.0.0"
    DEFAULT_API_PORT = 5000

    def __init__(self):

        app = Flask(__name__)
        api = Api(app)

        api.add_resource(RoboterResource, '/servo')

        app.run(host=Roboter.DEFAULT_API_BIND_ADDRESS,
                port=Roboter.DEFAULT_API_PORT, debug=False)
