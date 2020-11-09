import RPi.GPIO as GPIO
import time

button_pin =15

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# 깜빡거리는 코드  :4번 LED가 깜빡거림
#while 1: 
#			~~~


#버튼 누르면 button pushed!가 출력되는 코드
while 1:
	if GPIO.input(button_pin) == GPIO.HIGH:
		print("Button pushed!")
	time.sleep(0.1)
