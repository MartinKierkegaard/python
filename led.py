import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
#GPIO.setup(17, GPIO.OUT)
#GPIO.setup(27, GPIO.OUT)
#GPIO.setup(22, GPIO.OUT)
red = 1
green = 1
blue = 1
def setLight(r,g,b) :
	if (r == 1):
	 GPIO.output(14,GPIO.LOW)
	else:
	 GPIO.output(14,GPIO.HIGH)

	if (g==1):
	 GPIO.output(15,GPIO.LOW)
	else:
	 GPIO.output(15,GPIO.HIGH)
	if (b==1):
	 GPIO.output(18,GPIO.LOW)
	else:
	 GPIO.output(18,GPIO.HIGH)
	return


setLight(1,0,0)
time.sleep(0.5)
setLight(1,1,0)
time.sleep(0.5)
setLight(1,1,1)
time.sleep(0.5)
setLight(0,1,1)
time.sleep(0.5)
setLight(0,0,1)
time.sleep(0.5)
setLight(0,1,1)
time.sleep(2.5)
setLight(1,1,1)
time.sleep(0.5)
setLight(1,0,1)
time.sleep(0.5)
setLight(1,0,0)
time.sleep(0.5)
setLight(1,1,1)


setLight(0,0,0)#swith off lights
count = 0
#while(True) : 
#(count < 8) :
 # count = count +1 
#GPIO.output(14, GPIO.HIGH)
#GPIO.output(15, GPIO.HIGH)
#GPIO.output(18, GPIO.HIGH)
 # GPIO.output(17, GPIO.LOW)
 # GPIO.output(27, GPIO.HIGH)
 # GPIO.output(22, GPIO.HIGH)
 # time.sleep( 0.4 )
 # GPIO.output(14, GPIO.HIGH)
 # GPIO.output(15, GPIO.HIGH)
 # GPIO.output(18, GPIO.LOW)
 # GPIO.output(17, GPIO.HIGH)
 # GPIO.output(27, GPIO.LOW)
 # GPIO.output(22, GPIO.HIGH)
 # time.sleep(0.41)
 # GPIO.output(14, GPIO.HIGH)
 # GPIO.output(15, GPIO.LOW)
 # GPIO.output(18, GPIO.HIGH) 
 # time.sleep(0.21)

#GPIO.output(14, GPIO.HIGH)
#GPIO.output(15, GPIO.HIGH)
#GPIO.output(18, GPIO.HIGH)
#wait for input
input("Press Enter to continue...")
#reset pins
GPIO.cleanup()

