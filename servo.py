import RPi.GPIO as GPIO
import time

# The Control Class for SG92R
class ServoCtrl:
    def __init__(self, pin_num = 4):
        PWM_CYCLE = 50
        GPIO.setmode(GPIO.BCM)
        self.pin_output = pin_num
        GPIO.setup(self.pin_output, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin_output, PWM_CYCLE)
        self.servo.start(0)


    def set_deg(self, deg):
        D_MAX = 180
        D_MIN = 0
        if deg < D_MIN or deg > D_MAX:
            return False

        P_MAX = 12
        P_MIN = 2.5
        duty_range = (P_MAX - P_MIN) * (float(deg) / abs(D_MAX - D_MIN))
        duty = P_MIN + duty_range
        print("{0}, {1}".format(duty_range, duty))
        self.servo.ChangeDutyCycle(duty)
        return True

    def cleanup(self):
        self.set_deg(0)
        time.sleep(0.5)
        self.servo.stop()
        GPIO.cleanup()

    def test(self, duty):
        self.servo.ChangeDutyCycle(duty)

if __name__ == '__main__':
    ctrl = ServoCtrl()
    print("start")
    ret = ctrl.set_deg(90)
    print(ret)
    time.sleep(1)
    ctrl.set_deg(180)
    time.sleep(1)
    ctrl.set_deg(45)
    time.sleep(1)
    ctrl.cleanup()

