'''
딜레이를 사용하는 패키지
GPIO를 사용하는 패키지
'''
import time
import RPi.GPIO as GPIO

# GPIO23을 사용하겠다는 코드
pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO의 입력[충격]값은 1로 받도록 라즈베리 파이에서 설정해놓았다고 한다
# 그래서 조건을 1로 설정해놓으면 장땡
def crash_check():
	if GPIO.input(pin) == 1:
		crash_check_res = 1
	else:
		crash_check_res = 0
	
	return crash_check_res

# 패키지로 불러올때는 사용하지 않고 이 파일 자체만 실행시키면 돌아가는 코드
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
