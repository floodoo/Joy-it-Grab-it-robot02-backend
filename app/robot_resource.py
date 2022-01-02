from flask_restful import Resource
from flask import request
from app.servo import Servo
from app.sequence import Sequence
import Adafruit_PCA9685
import json
from time import sleep

class RobotResource(Resource):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.servo_liste = []
            cls.teaching_list = []
            cls._pwm = Adafruit_PCA9685.PCA9685(address=0x41)
            cls._pwm.set_pwm_freq(50)
            cls.sequence = Sequence()

            config_file = open("app/roboconfig.json")

            cls._config = json.load(config_file)

            if config_file is not None:
                config_file.close()
                servos_config = cls._config["servos"]

                for i in servos_config:
                    config = servos_config[i]
                    cls.servo_liste.append(
                        Servo(cls._pwm,
                              servo_id=config["id"],
                              pwm_min=config["pwm_min"],
                              pwm_max=config["pwm_max"],
                              pwm_neutral=config["pwm_neutral"],
                              pos_min=config["pos_min"],
                              pos_max=config["pos_max"],
                              pos_neutral=config["pos_neutral"],)
                    )
                for servo in cls.servo_liste:
                    servo.reset()

        return cls._instance

    def _get_servo_data(self):
        resource = {
            "servos": [],
            "teach": []
        }

        for servo in self.servo_liste:
            resource["servos"].append(
                {
                    "id": servo.get_id(),
                    "pos": servo.get_pos()
                }
            )

        resource["teach"].append(
            {
                "teaching": False,
                "run": False,
                "reset": False,
                "example": False
            }
        )

        return resource

    def get(self):
        data = self._get_servo_data()
        return data, 200

    def put(self):
        resource = request.json
        servo_data = resource["servos"]

        for data in servo_data:
            servo_id = int(data["id"])
            servo_position = data["pos"]

            for servo in self.servo_liste:
                if servo.get_id() == servo_id:
                    if servo_position != servo.get_pos():
                        servo.set_pos(servo_position)
                        
        teach = resource["teach"]

        for teach_answer in teach:
            if teach_answer["teaching"] == True:
                teach_answer["teaching"] = False
                liste = []

                for servo in self.servo_liste:
                    servo_get_id = servo.get_id()
                    servo_get_pos = servo.get_pos()
                    liste.append(servo_get_pos)
                    
                self.teaching_list.append(liste)

            if teach_answer["run"] == True:
                teach_answer["run"] = False

                for sequence in self.teaching_list:
                    counter = 0
                    sleep(0.7)

                    for position in sequence:
                        if counter <= 15:
                            servo = self.servo_liste[counter]
                            servo.set_pos(position)
                            counter += 1

            if teach_answer["reset"] == True:
                teach_answer["reset"] = False
                self.teaching_list = []

            if teach_answer["example"] == True:
                teach_answer["example"] = False
                example_data = self.sequence.sequence_1()
                keys = list(example_data["sequence_1"].keys())

                for i in keys:
                    position = example_data["sequence_1"][i]
                    
                    for i in position:
                        servo_position_id = i["id"]
                        servo_sequence_position = i["pos"]
                        servo_object = self.servo_liste[servo_position_id]
                        servo_object.set_pos(servo_sequence_position)
                        sleep(0.7)

        resource = self._get_servo_data()
        return resource, 200
