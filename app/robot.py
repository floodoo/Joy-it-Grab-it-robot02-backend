from app.robot_resource import RobotResource
from flask import Flask
from flask_restful import Api
from app.servo import Servo


class Robot():

    DEFAULT_API_BIND_ADDRESS = "0.0.0.0"
    DEFAULT_API_PORT = 5000

    def __init__(self):

        app = Flask(__name__)
        api = Api(app)

        api.add_resource(RobotResource, '/servo')

        app.run(host=Robot.DEFAULT_API_BIND_ADDRESS,
                port=Robot.DEFAULT_API_PORT, debug=False)
