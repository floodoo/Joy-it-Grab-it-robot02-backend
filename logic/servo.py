class Servo():
    SERVO_ID = 0
    PWM_MIN_LIMIT = 500
    PWM_MIN_DEFAULT = 1000
    PWM_NEUTRAL_DEFAULT = 1500
    PWM_MAX_LIMIT = 2500
    PWM_MAX_DEFAULT = 2000
    POS_MIN_DEFAULT = -1000
    POS_MAX_DEFAULT = 1000
    POS_NEUTRAL_DEFAULT = 0

    def __init__(self, pwm_controller, servo_id=SERVO_ID, pwm_min=PWM_MIN_DEFAULT, pwm_max=PWM_MAX_DEFAULT, pwm_neutral=PWM_NEUTRAL_DEFAULT, pos_min=POS_MIN_DEFAULT, pos_max=POS_MAX_DEFAULT, pos_neutral=POS_NEUTRAL_DEFAULT):

        self._pwm_controller = pwm_controller
        self._servo_id = servo_id
        self._pwm_min = pwm_min
        self._pwm_max = pwm_max
        self._pwm_neutral = pwm_neutral
        self._pos_min = pos_min
        self._pos_max = pos_max
        self._pos_neutral = pos_neutral
        self._pos_current = self._pos_neutral
        self._pwm_current = self._pwm_neutral

        self.set_pwm(self._pwm_current)

    def get_id(self):
        return self._servo_id

    def get_pwm_min(self):
        return self._pwm_min

    def set_pwm_min(self, pwm_min):
        if pwm_min >= Servo.PWM_MIN_LIMIT and pwm_min < self._pwm_max:
            self._pwm_min = pwm_min
        else:
            raise ValueError("Ungültiger pwm_min Parameterwert")

    def get_pwm_max(self):
        return self._pwm_max

    def set_pwm_max(self, pwm_max):
        if pwm_max > self._pwm_min and pwm_max <= Servo.PWM_MAX_LIMIT:
            self._pwm_max = pwm_max
        else:
            raise ValueError("Ungültiger pwm_max Parameterwert")

    def get_pwm_neutral(self):
        return self._pwm_neutral

    def set_pwm_neutral(self, pwm_neutral):
        if pwm_neutral >= self._pwm_min and pwm_neutral <= self._pwm_max:
            self._pwm_neutral = pwm_neutral
        else:
            raise ValueError("Ungültiger pwm_neutral Parameterwert")

    def get_pwm(self):
        return self._pwm_current

    def set_pwm(self, pwm):
        if pwm >= self._pwm_min and pwm <= self._pwm_max:
            pulse_length_per_bit = 1000000 / 50 / 4096
            pulse = int(round(pwm / pulse_length_per_bit))
            self._pwm_controller.set_pwm(self._servo_id, 0, pulse)
            self._pwm_current = pwm
        else:
            raise ValueError("Ungültiger pwm Parameterwert")

    def reset(self):
        self.set_pwm(self._pwm_neutral)

    def get_pos_min(self):
        return self._pos_min

    def set_pos_min(self, pos_min):
        if pos_min < self._pos_max:
            self._pos_min = pos_min
        else:
            raise ValueError("Ungültiger pos_min Parameterwert")

    def get_pos_max(self):
        return self._pos_max

    def set_pos_max(self, pos_max):
        if pos_max > self._pos_min:
            self._pos_max = pos_max
        else:
            raise ValueError("Ungültiger pos_max Parameterwert")

    def get_pos_neutral(self):
        return self._pos_neutral

    def set_pos_neutral(self, pos_neutral):
        if pos_neutral >= self._pos_min and pos_neutral <= self._pos_max:
            self._pos_neutral = pos_neutral
        else:
            raise ValueError("Ungültiger pos_neutral Parameterwert")

    def _calculate_pwm(self, x):
        if x < self._pos_neutral:
            m = (self._pwm_neutral - self._pwm_min) / \
                (self._pos_neutral - self._pos_min)
            t = self._pwm_neutral - m * self._pos_neutral
            y = m * x + t
        elif x == self._pos_neutral:
            y = self._pwm_neutral
        else:
            m = (self._pwm_max - self._pwm_neutral) / \
                (self._pos_max - self._pos_neutral)
            t = self._pwm_neutral - m * self._pos_neutral
            y = m * x + t
        y = round(y)
        y = int(y)
        return y

    def get_pos(self):
        return self._pos_current

    def set_pos(self, pos):
        if pos >= self._pos_min and pos <= self._pos_max:
            self._pos_current = pos
            new_pwm = self._calculate_pwm(pos)
            self.set_pwm(new_pwm)
        else:
            raise ValueError("ValueError: Ungültiger pos Parameterwert: pos_requested: {pos_requested}, pos_current: {pos_current}, pos_min: {pos_min}, pos_max: {pos_max}".format(
                pos_requested=pos,
                pos_current=self._pos_current,
                pos_min=self._pos_min,
                pos_max=self._pos_max))
