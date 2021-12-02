'''
시간 관련 패키지를 불러온다
라즈베리 파이 pin을 활성화 시키는 패키지를 불러온다
'''
import time
import RPi.GPIO as GPIO

# 라즈베리 파이의 핀을 활성화 시킨다
GPIO.setmode(GPIO.BCM)
# 사소한 오류 메세지를 무시하는 코드
GPIO.setwarnings(False)

# 현재 초음파 센서의 트리거핀은 'GPIO 24'에 연결되어 있고, 에코핀은 'GPIO 8'에 연결되도록 설정하였다
# 실제 라즈베리 파이 핀 도형도를 보면 GPIO 24는 '18'번핀, GPIO 8은 '24'번핀에 할당되었다
# 결론 = 초음파 센서를 도형도대로 18번핀 24번핀에 꼽고, 18번핀과 24번핀에 해당하는 GPIO 를 보고 값을 설정해야된다
GPIO_TRIGGER = 24
GPIO_ECHO = 8

# 대충 트리거는 출력을 담당하고 에코는 입력을 담당한다는 이야기인것으로 추정
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

# 거리를 구하는 클래스를 distance()라고 부르기로 하였어요
def distance():

    # 대충 0.00001초 마다 초음파 거리를 측정하겠다는 내용
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # [끝까지 코드의 해석] 대충 초음파 거리를 구하는 공식 ㅎㅎ;; 저도 잘 몰름
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    
    return distance

# sonicWave.py 자체를 실행하면 실행이되는 구절, 외부에서 함수로써 쓰면 실행 안된다.
# 대충 파일 자체로써 코드가 잘 작동하는지 알아볼 수 있는 코드
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()