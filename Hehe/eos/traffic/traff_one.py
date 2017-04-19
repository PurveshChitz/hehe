import time
import Adafruit_BBIO.GPIO as gpio

gpio.setup("P9_11", gpio.OUT)
gpio.setup("P9_13", gpio.OUT)
gpio.setup("P9_15", gpio.OUT)
gpio.setup("P9_24", gpio.OUT)

gpio.setup("P9_14", gpio.OUT)
gpio.setup("P9_16", gpio.OUT)
gpio.setup("P9_23", gpio.OUT)
gpio.setup("P9_12", gpio.OUT)

gpio.setup("P8_14", gpio.OUT)
gpio.setup("P8_16", gpio.OUT)
gpio.setup("P8_18", gpio.OUT)
gpio.setup("P8_12", gpio.OUT)

gpio.setup("P8_11", gpio.OUT)
gpio.setup("P8_13", gpio.OUT)
gpio.setup("P8_15", gpio.OUT)
gpio.setup("P8_17", gpio.OUT)

#North traffic fgpio.LOW
def northToSouth():

	
	
	
	gpio.output("P8_14", gpio.HIGH)	#green on
	gpio.output("P8_12", gpio.HIGH)	#left green on
	gpio.output("P8_16", gpio.LOW)
	gpio.output("P8_18", gpio.LOW)
	
	gpio.output("P8_11", gpio.HIGH)
	gpio.output("P8_13", gpio.LOW)
	gpio.output("P8_15", gpio.LOW)
	gpio.output("P8_17", gpio.LOW)
	
	gpio.output("P9_11", gpio.HIGH)
	gpio.output("P9_13", gpio.LOW)
	gpio.output("P9_15", gpio.LOW)
	gpio.output("P9_24", gpio.LOW)
	
	gpio.output("P9_23", gpio.HIGH)
	gpio.output("P9_16", gpio.LOW)
	gpio.output("P9_14", gpio.LOW)
	gpio.output("P9_12", gpio.LOW)
	
	#Time out for yelgpio.LOW
	time.sleep(10)
	gpio.output("P8_14", gpio.LOW)	#green on
	gpio.output("P8_12", gpio.LOW)	
	gpio.output("P8_16", gpio.HIGH)
	
	

#Right to left
def rightToLeft():
	gpio.output("P8_15", gpio.HIGH)	#green on
	gpio.output("P8_17", gpio.HIGH)	#left green on
	gpio.output("P8_11", gpio.LOW)
	gpio.output("P8_13", gpio.LOW)
	
	gpio.output("P8_18", gpio.HIGH)
	gpio.output("P8_16", gpio.LOW)
	gpio.output("P8_14", gpio.LOW)
	gpio.output("P8_12", gpio.LOW)
	
	gpio.output("P9_11", gpio.HIGH)
	gpio.output("P9_13", gpio.LOW)
	gpio.output("P9_15", gpio.LOW)
	gpio.output("P9_24", gpio.LOW)
	
	gpio.output("P9_23", gpio.HIGH)
	gpio.output("P9_16", gpio.LOW)
	gpio.output("P9_14", gpio.LOW)
	gpio.output("P9_12", gpio.LOW)
	
	#Time out for yelgpio.LOW
	time.sleep(10)
	gpio.output("P8_15", gpio.LOW)	#green on
	gpio.output("P8_17", gpio.LOW)
	gpio.output("P8_13", gpio.HIGH)
	
	
#South to north
def southToNorth():
	gpio.output("P8_14", gpio.LOW)	#green on
	gpio.output("P8_12", gpio.LOW)	#left green on
	gpio.output("P8_16", gpio.LOW)
	gpio.output("P8_18", gpio.HIGH)
	
	gpio.output("P8_11", gpio.HIGH)
	gpio.output("P8_13", gpio.LOW)
	gpio.output("P8_15", gpio.LOW)
	gpio.output("P8_17", gpio.LOW)
	
	gpio.output("P9_11", gpio.LOW)
	gpio.output("P9_13", gpio.LOW)
	gpio.output("P9_15", gpio.HIGH)
	gpio.output("P9_24", gpio.HIGH)
	
	gpio.output("P9_23", gpio.HIGH)
	gpio.output("P9_16", gpio.LOW)
	gpio.output("P9_14", gpio.LOW)
	gpio.output("P9_12", gpio.LOW)
	
	#Time out for yelgpio.LOW
	time.sleep(10)
	gpio.output("P9_15", gpio.LOW)
	gpio.output("P9_24", gpio.LOW)
	gpio.output("P9_13", gpio.HIGH)

	
#Left to right
def leftToRight():
	gpio.output("P8_14", gpio.LOW)	#green on
	gpio.output("P8_12", gpio.LOW)	#left green on
	gpio.output("P8_16", gpio.LOW)
	gpio.output("P8_18", gpio.HIGH)
	
	gpio.output("P8_11", gpio.HIGH)
	gpio.output("P8_13", gpio.LOW)
	gpio.output("P8_15", gpio.LOW)
	gpio.output("P8_17", gpio.LOW)
	
	gpio.output("P9_11", gpio.HIGH)
	gpio.output("P9_13", gpio.LOW)
	gpio.output("P9_15", gpio.LOW)
	gpio.output("P9_24", gpio.LOW)
	
	gpio.output("P9_23", gpio.LOW)
	gpio.output("P9_16", gpio.LOW)
	gpio.output("P9_14", gpio.HIGH)
	gpio.output("P9_12", gpio.HIGH)
	
	#Time out for yelgpio.LOW
	time.sleep(10)
	gpio.output("P9_14", gpio.LOW)
	gpio.output("P9_12", gpio.LOW)
	gpio.output("P9_16", gpio.HIGH)
	
	
	
#Main function
print "Execution started...."

#Repeat signal functions 5 times
for i in range (0, 5):
	print "North to south..."
	northToSouth()
	time.sleep(1)
	print "Right to left..."
	rightToLeft()
	time.sleep(1)
	print "South to north..."
	southToNorth()
	time.sleep(1)
	print "Left to right..."
	leftToRight()
	time.sleep(1)

print "Traffic signal execution done......!"

