import Adafruit_BBIO.GPIO as gpio
import Adafruit_PWM as pwm
import time
pwm.start("P8_13",50)
while 1:
	pwm.set_duty_cycle("P8_13",0)
	time.sleep(0.5)
	pwm.set_duty_cycle("P8_13",20)
	time.sleep(0.5)
	pwm.set_duty_cycle("P8_13",50)
	time.sleep(0.5)
	pwm.set_duty_cycle("P8_13",80)
	time.sleep(0.5)
pwm.stop("P8_13")
pwm.cleanup()