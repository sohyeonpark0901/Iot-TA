import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG=23
ECHO=24
print("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG,True)
        time.sleep(0.0001)
        GPIO.output(TRIG,False)
        
        
        while GPIO.input(ECHO)==0:
            start = time.time()
        while GPIO.input(ECHO)==1:
            stop = time.time()
        print(type(stop))
        
        check_time = stop - start
        distance = check_time * 3420 /2
        print("Distance : %.1f cm" %distance)
        time.sleep(0.4)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()      
                
