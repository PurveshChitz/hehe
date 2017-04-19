import Adafruit_BBIO.GPIO as GPIO
import time


lift_status=0



GPIO.setup("P8_11",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P8_13",GPIO.OUT)
GPIO.setup("P8_14",GPIO.OUT)
GPIO.setup("P8_15",GPIO.OUT)
GPIO.setup("P8_16",GPIO.OUT)
GPIO.setup("P8_17",GPIO.OUT)
GPIO.setup("P8_18",GPIO.OUT)
GPIO.setup("P8_19",GPIO.OUT)                                                    
GPIO.setup("P8_21",GPIO.OUT)                                                    

GPIO.setup("P9_11",GPIO.OUT) 
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_13",GPIO.OUT) 
GPIO.setup("P9_14",GPIO.OUT) 
GPIO.setup("P9_15",GPIO.OUT)
GPIO.setup("P9_16",GPIO.OUT) 
GPIO.setup("P9_23",GPIO.OUT)                                                    
GPIO.setup("P9_24",GPIO.OUT)                                                    
GPIO.setup("P8_7",GPIO.IN) 
GPIO.setup("P8_8",GPIO.IN)
GPIO.setup("P8_9",GPIO.IN)
GPIO.setup("P8_10",GPIO.IN)


GPIO.output("P8_11",GPIO.LOW)
GPIO.output("P8_12",GPIO.LOW)
GPIO.output("P8_13",GPIO.LOW)
GPIO.output("P8_14",GPIO.LOW)
GPIO.output("P8_15",GPIO.LOW)
GPIO.output("P8_16",GPIO.LOW)
GPIO.output("P8_17",GPIO.LOW)
GPIO.output("P8_18",GPIO.LOW)
GPIO.output("P8_19",GPIO.LOW)
GPIO.output("P8_21",GPIO.LOW)

GPIO.output("P9_11",GPIO.LOW)
GPIO.output("P9_12",GPIO.LOW)
GPIO.output("P9_13",GPIO.LOW)
GPIO.output("P9_14",GPIO.LOW)
GPIO.output("P9_15",GPIO.LOW)
GPIO.output("P9_16",GPIO.LOW)
GPIO.output("P9_23",GPIO.LOW)



 
time.sleep(1)

def zero():
        GPIO.output("P8_17",GPIO.HIGH)
        GPIO.output("P8_11",GPIO.LOW)
        GPIO.output("P8_12",GPIO.LOW)
        GPIO.output("P8_13",GPIO.LOW)
        GPIO.output("P8_14",GPIO.LOW)
        GPIO.output("P8_15",GPIO.LOW)
        GPIO.output("P8_16",GPIO.LOW)
        GPIO.output("P8_18",GPIO.HIGH)
def one():
        GPIO.output("P8_17",GPIO.HIGH)
        GPIO.output("P8_11",GPIO.HIGH)
        GPIO.output("P8_12",GPIO.LOW)
        GPIO.output("P8_13",GPIO.LOW)
        GPIO.output("P8_14",GPIO.HIGH)
        GPIO.output("P8_15",GPIO.HIGH)
        GPIO.output("P8_16",GPIO.HIGH)
        GPIO.output("P8_18",GPIO.HIGH)
def two():
        GPIO.output("P8_17",GPIO.LOW)
        GPIO.output("P8_11",GPIO.LOW)
        GPIO.output("P8_12",GPIO.LOW)
        GPIO.output("P8_13",GPIO.HIGH)
        GPIO.output("P8_14",GPIO.LOW)
        GPIO.output("P8_15",GPIO.LOW)
        GPIO.output("P8_16",GPIO.HIGH)
        GPIO.output("P8_18",GPIO.HIGH)
def three():
        GPIO.output("P8_17",GPIO.LOW)
        GPIO.output("P8_11",GPIO.LOW)
        GPIO.output("P8_12",GPIO.LOW)
        GPIO.output("P8_13",GPIO.LOW)
        GPIO.output("P8_14",GPIO.LOW)
        GPIO.output("P8_15",GPIO.HIGH)
        GPIO.output("P8_16",GPIO.HIGH)
        GPIO.output("P8_18",GPIO.HIGH)

def glow_green():
	GPIO.output("P9_12",GPIO.HIGH)
	GPIO.output("P9_14",GPIO.HIGH)
	GPIO.output("P9_16",GPIO.HIGH)
	GPIO.output("P9_23",GPIO.HIGH)
	GPIO.output("P9_11",GPIO.LOW)
	GPIO.output("P9_13",GPIO.LOW)
	GPIO.output("P9_15",GPIO.LOW)
	GPIO.output("P9_24",GPIO.LOW)

def glow_yellow():
	GPIO.output("P9_12",GPIO.LOW)
	GPIO.output("P9_14",GPIO.LOW)
	GPIO.output("P9_16",GPIO.LOW)
	GPIO.output("P9_23",GPIO.LOW)
	GPIO.output("P9_11",GPIO.HIGH)
	GPIO.output("P9_13",GPIO.HIGH)
	GPIO.output("P9_15",GPIO.HIGH)
	GPIO.output("P9_24",GPIO.HIGH)
zero()
time.sleep(1)
while True:
	if GPIO.input("P8_7")==0:
		if lift_status==0:
			glow_yellow()
			zero()
			time.sleep(1)
			one()
			time.sleep(1)
			two()
			time.sleep(1)
			three()
			time.sleep(1)
		elif lift_status==1:
			glow_yellow()
			one()
			time.sleep(1)
			two()
			time.sleep(1)
			three()
			time.sleep(1)
		elif lift_status==2:
			glow_yellow()
			two()
			time.sleep(1)
			three()
			time.sleep(1)
		lift_status=3
	elif GPIO.input("P8_9")==0:
		if lift_status==0:
			glow_yellow()
			zero()
			time.sleep(1)
			one()
			time.sleep(1)
			two()
			time.sleep(1)
		elif lift_status==1:
			glow_yellow()
			one()
			time.sleep(1)
			two()
			time.sleep(1)
		elif lift_status==3:
			glow_green()
			three()
			time.sleep(1)
			two()
			time.sleep(1)
		lift_status=2
	elif GPIO.input("P8_8")==0:
		if lift_status==0:
			glow_yellow()
			zero()
			time.sleep(1)
			one()
			time.sleep(1)
		elif lift_status==2:
			glow_green()
			two()
			time.sleep(1)
			one()
			time.sleep(1)
		elif lift_status==3:
			glow_green()
			three()
			time.sleep(1)
			two()
			time.sleep(1)
			one()
			time.sleep(1)
		lift_status=1			
	elif GPIO.input("P8_10")==0:
		if lift_status==1:
			glow_green()
			one()
			time.sleep(1)
			zero()
			time.sleep(1)
		elif lift_status==2:
			glow_green()
			two()
			time.sleep(1)
			one()
			time.sleep(1)
			zero()
			time.sleep(1)
		elif lift_status==3:
			glow_green()
			three()
			time.sleep(1)
			two()
			time.sleep(1)
			one()
			time.sleep(1)
			zero()
			time.sleep(1)
		lift_status=0
