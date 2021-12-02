# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def crash_check():
	if GPIO.input(pin) == 1:
		crash_check_res = 1
	else:
		crash_check_res = 0
	
	return crash_check_res

if __name__ == '__main__':
	try:
		while True:
			result = crash_check()
			if result == 1:
				print("진동이 감지 되었습니다.")
				time.sleep(1)
			else:
				print("진동이 없습니다.")
				time.sleep(1)
            
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()
